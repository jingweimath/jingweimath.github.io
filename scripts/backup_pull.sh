#!/bin/bash
# 经纬考研数学 · 本地备份拉取脚本（Git Bash 下运行）
#   1) 让服务器生成一份最新备份
#   2) 拉到本机桌面 jingweimath-backup/<时间戳>/server
#   3) 本机再把题库源文件打包进 <时间戳>/local-source
# 用法：bash scripts/backup_pull.sh
set -e

HOST="root@62.234.131.123"
REMOTE_DIR="/root/backups"
LOCAL_ROOT="/c/Users/yuwei/Desktop/jingweimath-backup"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
WORKSPACE="/c/Users/yuwei/WorkBuddy/2026-10-16-10-10-50"

STAMP=$(date +%Y%m%d-%H%M%S)
DEST="$LOCAL_ROOT/$STAMP"
mkdir -p "$DEST/server" "$DEST/local-source"

echo "[1/4] 服务器生成备份中..."
LATEST=$(ssh -o StrictHostKeyChecking=no "$HOST" \
  "bash /root/backup_jingweimath.sh >/dev/null 2>&1; ls -1dt $REMOTE_DIR/jm-* | head -1")
echo "      $LATEST"

echo "[2/4] 拉取到本地..."
scp -o StrictHostKeyChecking=no -q -r "$HOST:$LATEST/" "$DEST/server/"

echo "[3/4] 打包本机题库源文件..."
tar czf "$DEST/local-source/questions.tar.gz" -C "$REPO" questions build_questions.py
cp "$REPO/questions-bundle-v2.js" "$DEST/local-source/" 2>/dev/null || true
if [ -d "$WORKSPACE/outputs" ]; then
  tar czf "$DEST/local-source/outputs.tar.gz" -C "$WORKSPACE" outputs
fi
if [ -d "$WORKSPACE/题库_扩展" ]; then
  tar czf "$DEST/local-source/题库扩展.tar.gz" -C "$WORKSPACE" 题库_扩展
fi

echo "[4/4] 写摘要..."
{
  echo "=== 经纬考研数学备份 $(date '+%F %T') ==="
  echo "服务器包: $LATEST"
  echo "--- 本机内容 ---"
  du -h "$DEST"/server/* "$DEST"/local-source/* 2>/dev/null
  echo "--- 题库指纹（应与服务器一致）---"
  md5sum "$REPO/questions-bundle-v2.js" 2>/dev/null
} > "$DEST/README.txt"

echo
echo "备份完成：$DEST"
du -sh "$DEST"
cat "$DEST/README.txt"
