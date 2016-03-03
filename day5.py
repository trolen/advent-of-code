#!/usr/bin/env python3

import fileinput

DISALLOWED=['ab','cd','pq','xy']

def is_nice1(line):
  for s in DISALLOWED:
    if s in line:
      return False
  vowel_count = 0
  double_letter = False
  prev_c = ''
  for c in line:
    if c in 'aeiou':
      vowel_count += 1
    if c == prev_c:
      double_letter = True
    prev_c = c
  return vowel_count >= 3 and double_letter

def is_nice2(line):
  repeated_letter = False
  repeated_string = False
  prev_c1 = ''
  prev_c2 = ''
  for c in line:
    if prev_c1 != '' and line.count(prev_c1 + c) >= 2:
      repeated_string = True
    if c == prev_c2:
      repeated_letter = True
    prev_c2 = prev_c1
    prev_c1 = c
  return repeated_string and repeated_letter

if __name__ == "__main__":
  nice1 = 0
  nice2 = 0
  for line in fileinput.input():
    if is_nice1(line):
      nice1 += 1
    if is_nice2(line):
      nice2 += 1
  print("Nice strings #1: %s" % nice1)
  print("Nice strings #2: %s" % nice2)
