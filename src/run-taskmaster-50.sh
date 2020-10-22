#!/bin/zsh

for i in {5..100}; do 
  python3 precondition-check.py --filename taskmaster-$i.csv
done
