#!/usr/bin/env python3

import fileinput
import sys

def find_combinations(amt_to_store, containers):
  combos = []
  for i in range(len(containers)):
    amt = amt_to_store - containers[i]
    if amt == 0:
      combos.append([containers[i]])
    elif amt > 0:
      for f in find_combinations(amt, containers[i+1:]):
        combos.append([containers[i]] + f)
  return combos

def count_all_combos(amt_to_store, containers):
  return len(find_combinations(amt_to_store, containers))

def count_min_combos(amt_to_store, containers):
  lengths = [len(c) for c in find_combinations(amt_to_store, containers)]
  min_length = min(lengths)
  return lengths.count(min_length)

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  containers = [int(x) for x in read_input()]
  containers.sort(reverse = True)
  print("Combinations: %s" % count_all_combos(150, containers))
  print("Minimum: %s" % count_min_combos(150, containers))
