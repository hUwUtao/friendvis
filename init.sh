#!/bin/bash

MASTER=hUwUtao

pyp() {
  python ran.py $1 $2
  # not necessary, since root, which contains all already get the full one
  # ./p5pic.sh $2/$1
}

mkdir -p data/child

pyp "$MASTER" data # root node (0vis in visgraph)

cat "data/$MASTER.json" | jq -r .[].li | tr -d '\r' | while read l; do
  pyp "$l" data/child
done

pypy mkcsv.py $MASTER