#!/usr/bin/env python

import fileinput

def main():
  floor = 0
  position = 0
  positionEnterBasement = 0
  for line in fileinput.input():
    for c in line:
      if c == '(':
        floor += 1
      if c == ')':
        floor -= 1
      position += 1
      if floor < 0 and positionEnterBasement <= 0:
        positionEnterBasement = position
  print "Final floor:", floor
  print "Entered basement at position:", positionEnterBasement

if __name__ == "__main__":
  main()
