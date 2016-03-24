#!/usr/bin/env python3

import fileinput
import sys

def store_eggnog(amt_to_store, containers):
  if amt_to_store == 0:
    return 1
  count = 0
  for i in range(len(containers)):
    amt = amt_to_store - containers[i]
    count += store_eggnog(amt, containers[i+1:])
  return count

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  containers = [int(x) for x in read_input()]
  containers.sort(reverse = True)
  print(store_eggnog(150, containers))
