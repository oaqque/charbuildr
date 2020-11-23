#!/bin/zsh

for i in {0..200}; do 
  python ../agentonagent.py --model rick-and-morty --outfn rick-$i.csv
done
