#!/usr/bin/env zsh
b=$1; cap=${2:-62}
start=$(( (b-1)*50 + 1 )); end=$(( b*50 ))
i=$start
sed -n "${start},${end}p" audit/_filelist.txt | while IFS= read -r f; do
  printf '\n===== IDX %d | %s =====\n' "$i" "$f"
  head -n "$cap" "$f"
  i=$((i+1))
done
