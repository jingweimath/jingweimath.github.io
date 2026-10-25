#!/bin/bash
# 经纬考研数学网站备份脚本（服务器端）
# 用法：bash /root/backup_jingweimath.sh
# 产出：/root/backups/jm-YYYYMMDD-HHMMSS/{www,nginx,letsencrypt,scripts}.tar.gz + MANIFEST.txt
set -e

DATE=$(date +%Y%m%d)
TS=$(date +%H%M%S)
DEST=/root/backups
WORK="$DEST/jm-$DATE-$TS"

mkdir -p "$WORK"

# 1. 整站（排除历次 .bak-* 备份，那只是上线时的临时快照，留最新版即可）
tar czf "$WORK/www.tar.gz" --exclude='*.bak-*' -C /var/www jingweimath 2>/dev/null

# 2. nginx 配置（含 conf.d、证书引用）
tar czf "$WORK/nginx.tar.gz" -C /etc nginx 2>/dev/null

# 3. Let's Encrypt 证书
if [ -d /etc/letsencrypt ]; then
  tar czf "$WORK/letsencrypt.tar.gz" -C /etc letsencrypt 2>/dev/null
fi

# 4. /root 下的运维脚本（baidu_push.sh 等），不碰 .ssh
SCRIPTS=$(cd /root && ls *.sh 2>/dev/null || true)
if [ -n "$SCRIPTS" ]; then
  tar czf "$WORK/scripts.tar.gz" -C /root $SCRIPTS 2>/dev/null
fi

# 5. 清单：文件体积、题库指纹、关键版本
{
  echo "=== 备份时间: $(date '+%F %T') ==="
  echo "--- 内容体积 ---"
  du -h "$WORK"/*.tar.gz 2>/dev/null
  echo "--- 题库指纹 ---"
  md5sum /var/www/jingweimath/questions-bundle-v2.js 2>/dev/null
  echo -n "题库题数: "
  grep -o '"id": *"[a-zA-Z0-9_-]*"' /var/www/jingweimath/questions-bundle-v2.js 2>/dev/null | wc -l
  echo "--- practice.html 引用的 bundle 版本 ---"
  grep -o 'questions-bundle-v2.js?v=[0-9a-z]*' /var/www/jingweimath/practice.html 2>/dev/null | head -1
  echo "--- 系统 ---"
  nginx -v 2>&1
  df -h / | tail -1
} > "$WORK/MANIFEST.txt" 2>&1

# 6. 清理：保留最近 10 份，删除 14 天前的
find "$DEST" -maxdepth 1 -type d -name 'jm-*' -mtime +14 -exec rm -rf {} + 2>/dev/null || true
ls -1d "$DEST"/jm-* 2>/dev/null | sort | head -n -10 | xargs -r rm -rf

echo "备份完成: $WORK"
du -sh "$WORK"
cat "$WORK/MANIFEST.txt"
