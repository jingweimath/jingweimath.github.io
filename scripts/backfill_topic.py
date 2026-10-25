"""用 bundle 的 qid->topic/cat 映射，回填 attempt 表里 topic/cat 为空的历史记录。"""
import re, io, sqlite3, sys

bundle_path = sys.argv[1] if len(sys.argv) > 1 else 'questions-bundle-v2.js'
db_path = sys.argv[2] if len(sys.argv) > 2 else '/opt/jmstats/stats.db'

s = io.open(bundle_path, encoding='utf-8').read()

# 题目对象里 id/topic/cat 的相对顺序：id 在前，topic/cat 在后
mapping = {}
for m in re.finditer(r'"id":\s*"((?:cal|la|prob|comp)-[A-Za-z0-9\-]+)"', s):
    qid = m.group(1)
    seg = s[m.end():m.end() + 1500]
    tm = re.search(r'"topic":\s*"([^"]*)"', seg)
    cm = re.search(r'"cat":\s*"([^"]*)"', seg)
    if qid not in mapping:
        mapping[qid] = (cm.group(1) if cm else '', tm.group(1) if tm else '')

print('bundle 题号映射:', len(mapping))

con = sqlite3.connect(db_path)
cur = con.cursor()
rows = cur.execute(
    "SELECT rowid, qid, cat, topic FROM attempt WHERE topic IS NULL OR topic='' OR cat IS NULL OR cat=''"
).fetchall()
print('待回填记录:', len(rows))

n = 0
for rowid, qid, cat, topic in rows:
    c, t = mapping.get(qid, ('', ''))
    if not t and not c:
        continue
    cur.execute(
        "UPDATE attempt SET cat=?, topic=? WHERE rowid=?",
        (c or cat or '', t or topic or '', rowid)
    )
    n += 1
con.commit()
print('已回填:', n)

for r in cur.execute("SELECT qid, correct, diff, topic FROM attempt ORDER BY rowid"):
    print('  ', r)
con.close()
