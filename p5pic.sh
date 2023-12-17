#!/bin/bash
mkdir -p images

cat $1.json | jq ". | map([.img, .li] | join(\"|\")) | .[]" -r | tr -d '\r' | while IFS=\|  read -r p u; do
  OUTFS="images/${u}.jpg"
  echo \> $OUTFS
  if [[ ! -f "$OUTFS" ]]; then
    echo fetch
    curl "$p" -sSo "$OUTFS"
  else
    echo exist
  fi
done