#!/usr/bin/env python3

import fileinput
import sys

def store_eggnog(max_amt, containers):
  containers.sort(reverse=True)
  count = 0
  amt_left = max_amt
  for i in range(len(containers)):
    amt_left -= containers[i]
    if amt_left > 0:
      continue
    if amt_left == 0:
      count += 1
    if amt_left <= 0:
      amt_left += containers[i]
  return count

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  containers = [int(x) for x in read_input()]
  print(store_eggnog(150, containers))
