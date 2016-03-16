#!/usr/bin/env python3

import fileinput
import sys

def elevator_iter(s):
  floor = 0
  for c in s:
    if c == '(':
      floor += 1
    if c == ')':
      floor -= 1
    yield floor

def elevator(s):
  if len(s) > 0:
    return [x for x in elevator_iter(s)][-1]
  return 0

def enter_basement(s):
  if len(s) > 0:
    return list(p for (p,f) in enumerate(elevator_iter(s)) if f == -1)[0] + 1
  return None

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return ''.join([line.rstrip() for line in fileinput.input()])

if __name__ == "__main__":
  s = read_input()
  print('Final floor: %s' % elevator(s))
  print('Position entered basement: %s' % enter_basement(s))
