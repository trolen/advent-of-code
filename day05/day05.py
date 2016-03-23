#!/usr/bin/env python3

import fileinput
import sys
import re

def disallowed(line):
  return re.compile(r'ab|cd|pq|xy').search(line) != None

def vowel_count(line):
  return len(re.findall(r'[aeiou]', line))

def double_letter(line):
  return re.compile(r'([a-z])\1').search(line) != None

def is_nice1(line):
  return not disallowed(line) and vowel_count(line) >= 3 and double_letter(line)

def repeated_string(line):
  return re.compile(r'([a-z][a-z]).*\1').search(line) != None

def repeated_letter(line):
  return re.compile(r'([a-z]).\1').search(line) != None

def is_nice2(line):
  return repeated_string(line) and repeated_letter(line)

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
