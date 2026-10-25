#!/usr/bin/env python3
# 经纬考研数学 · 答题数据采集服务
# 监听 127.0.0.1:8787，由 nginx 反代 /api/
#   POST /api/report   匿名上报答题结果（不含任何个人信息）
#   GET  /api/stats    统计查询（需 token）
#   GET  /api/health   健康检查
import json
import os
import re
import sqlite3
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DB_PATH = '/opt/jmstats/stats.db'
TOKEN = os.environ.get('JM_STATS_TOKEN', 'jw2026stats')
PORT = int(os.environ.get('JM_STATS_PORT', '8787'))
MAX_BODY = 256 * 1024
MAX_ITEMS = 80
QID_RE = re.compile(r'^[A-Za-z0-9_\-]{1,48}$')

_local = threading.local()


def db():
    if not hasattr(_local, 'conn'):
        conn = sqlite3.connect(DB_PATH, timeout=10)
        conn.execute('PRAGMA journal_mode=WAL')
        _local.conn = conn
    return _local.conn


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS attempt (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            ts      INTEGER NOT NULL,
            uid     TEXT NOT NULL,
            qid     TEXT NOT NULL,
            correct INTEGER NOT NULL,
            diff    TEXT,
            cat     TEXT,
            topic   TEXT,
            sec     INTEGER,
            mode    TEXT
        );
        CREATE INDEX IF NOT EXISTS ix_qid   ON attempt(qid);
        CREATE INDEX IF NOT EXISTS ix_ts    ON attempt(ts);
        CREATE INDEX IF NOT EXISTS ix_topic ON attempt(topic);
    ''')
    conn.commit()
    conn.close()


RATE = {}
RATE_LOCK = threading.Lock()


def allow(ip, limit=30, window=10):
    now = time.time()
    with RATE_LOCK:
        arr = RATE.setdefault(ip, [])
        arr[:] = [t for t in arr if now - t < window]
        if len(arr) >= limit:
            return False
        arr.append(now)
        if len(RATE) > 5000:
            for k in list(RATE)[:2000]:
                RATE.pop(k, None)
    return True


def rows_to_dicts(rows):
    return [{'k': a, 'n': b, 'w': c} for a, b, c in rows if a]


class Handler(BaseHTTPRequestHandler):
    server_version = 'jm-stats'

    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path.split('?')[0].rstrip('/') != '/api/report':
            self._json({'error': 'not found'}, 404)
            return
        ip = self.headers.get('X-Real-IP') or self.client_address[0]
        if not allow(ip):
            self._json({'error': 'rate limit'}, 429)
            return
        try:
            length = int(self.headers.get('Content-Length') or 0)
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY:
            self._json({'error': 'bad body'}, 400)
            return
        try:
            data = json.loads(self.rfile.read(length).decode('utf-8'))
        except Exception:
            self._json({'error': 'bad json'}, 400)
            return

        uid = str(data.get('uid', ''))[:40]
        mode = str(data.get('mode', ''))[:24]
        items = data.get('items')
        if not uid or not isinstance(items, list) or len(items) > MAX_ITEMS:
            self._json({'error': 'bad payload'}, 400)
            return

        ts = int(time.time())
        rows = []
        for it in items:
            if not isinstance(it, dict):
                continue
            qid = str(it.get('id', ''))[:48]
            if not QID_RE.match(qid):
                continue
            try:
                sec = int(it.get('sec') or 0)
            except (TypeError, ValueError):
                sec = 0
            rows.append((
                ts, uid, qid, 1 if it.get('ok') else 0,
                str(it.get('diff', ''))[:16],
                str(it.get('cat', ''))[:48],
                str(it.get('topic', ''))[:80],
                min(sec, 7200), mode,
            ))
        if rows:
            conn = db()
            conn.executemany(
                'INSERT INTO attempt(ts,uid,qid,correct,diff,cat,topic,sec,mode) '
                'VALUES(?,?,?,?,?,?,?,?,?)', rows)
            conn.commit()
        self._json({'ok': True, 'n': len(rows)})

    def do_GET(self):
        path = self.path.split('?')[0].rstrip('/')
        qs = self.path.split('?', 1)[1] if '?' in self.path else ''
        if path == '/api/health':
            self._json({'ok': True})
            return
        if path != '/api/stats':
            self._json({'error': 'not found'}, 404)
            return
        params = {}
        for part in qs.split('&'):
            if '=' in part:
                k, v = part.split('=', 1)
                params[k] = v
        if params.get('token', '') != TOKEN:
            self._json({'error': 'forbidden'}, 403)
            return

        try:
            since = int(params.get('since', '0') or 0)
        except ValueError:
            since = 0
        where = ' WHERE ts >= ?' if since else ''
        args = (since,) if since else ()

        conn = db()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*), COUNT(DISTINCT uid), COUNT(DISTINCT qid) FROM attempt')
        total, users, covered = cur.fetchone()
        cur.execute('SELECT MIN(ts), MAX(ts) FROM attempt')
        tmin, tmax = cur.fetchone()

        def group(col, limit):
            cur.execute(
                'SELECT {c}, COUNT(*), SUM(CASE WHEN correct=0 THEN 1 ELSE 0 END) '
                'FROM attempt{w} GROUP BY {c} ORDER BY COUNT(*) DESC LIMIT ?'.format(c=col, w=where),
                args + (limit,))
            return rows_to_dicts(cur.fetchall())

        cur.execute(
            'SELECT date(ts,\'unixepoch\',\'+8 hours\') d, COUNT(*), '
            'SUM(CASE WHEN correct=0 THEN 1 ELSE 0 END) FROM attempt{w} '
            'GROUP BY d ORDER BY d DESC LIMIT 30'.format(w=where), args)
        daily = [{'d': a, 'n': b, 'w': c} for a, b, c in cur.fetchall()]

        self._json({
            'total': total,
            'users': users,
            'covered': covered,
            'first_ts': tmin,
            'last_ts': tmax,
            'top_wrong': group('qid', 100),
            'by_topic': group('topic', 80),
            'by_cat': group('cat', 40),
            'by_diff': group('diff', 10),
            'daily': daily,
        })


def main():
    init_db()
    server = ThreadingHTTPServer(('127.0.0.1', PORT), Handler)
    server.daemon_threads = True
    print('jm-stats listening on 127.0.0.1:%d' % PORT, flush=True)
    server.serve_forever()


if __name__ == '__main__':
    main()
