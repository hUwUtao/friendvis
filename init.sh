#!/bin/bash

MASTER=hUwUtao

pyp() {
  python ran.py $1 $2
  # weird behavior: added _ before .jpg? (maybe the null-t or eol, prob jq/gnubash broke sth)
  ./p5pic.sh $2/$1
}

mkdir -p data/child

pyp "$MASTER" data # root node (0vis in visgraph)

cat "data/$MASTER.json" | jq -r .[].li | tr -d '\r' | while read l; do
  pyp "$l" data/child
done