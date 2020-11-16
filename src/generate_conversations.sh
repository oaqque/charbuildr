#!/bin/zsh

for i in {0..30}; do 
  python3.6 agentonagent.py --model rick-and-morty --outfn rick-$i.csv
done
