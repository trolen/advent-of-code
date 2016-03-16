#!/usr/bin/env python3

import fileinput
import sys

def is_disallowed(line):
  for s in ['ab','cd','pq','xy']:
    if s in line:
      return True
  return False

def walk_string(s):
  c1 = ''
  c2 = ''
  for c in s:
    yield (c, c1, c2)
    c2 = c1
    c1 = c

def is_nice1(line):
  if is_disallowed(line):
    return False
  vowel_count = 0
  double_letter = False
  for (c, c1, c2) in walk_string(line):
    if c in 'aeiou':
      vowel_count += 1
    if c == c1:
      double_letter = True
  return vowel_count >= 3 and double_letter

def is_nice2(line):
  repeated_letter = False
  repeated_string = False
  for (c, c1, c2) in walk_string(line):
    if c1 != '' and line.count(c1 + c) >= 2:
      repeated_string = True
    if c == c2:
      repeated_letter = True
  return repeated_string and repeated_letter

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  nice1 = 0
  nice2 = 0
  lines = read_input()
  for line in lines:
    if is_nice1(line):
      nice1 += 1
    if is_nice2(line):
      nice2 += 1
  print("Nice strings #1: %s" % nice1)
  print("Nice strings #2: %s" % nice2)
