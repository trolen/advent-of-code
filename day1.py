#!/usr/bin/env python

import fileinput

def elevator(s):
  floor = 0
  for c in s:
    if c == '(':
      floor += 1
    if c == ')':
      floor -= 1
  return floor

def enter_basement(s):
  floor = 0
  position = 0
  for c in s:
    position += 1
    if c == '(':
      floor += 1
    if c == ')':
      floor -= 1
    if floor < 0:
      return position
  return None

if __name__ == "__main__":
  s = fileinput.input()[0]
  print 'Final floor:', elevator(s)
  print 'Position entered basement:', enter_basement(s)
