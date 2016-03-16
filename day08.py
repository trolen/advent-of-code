#!/usr/bin/env python3

import fileinput
import sys

def calc_code_length(s):
  return len(s)

def calc_mem_length(s):
  return len(eval(s))

def calc_encoded_length(s):
  result = '"'
  for c in s:
    if c in '"\\':
      result += '\\'
    result += c
  result += '"'
  return len(result)

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.strip() for line in fileinput.input()]

if __name__ == "__main__":
  total_code = 0
  total_mem = 0
  total_encoded = 0
  lines = read_input()
  for line in lines:
    total_code += calc_code_length(line)
    total_mem += calc_mem_length(line)
    total_encoded += calc_encoded_length(line)
  print("Code: %s" % total_code)
  print("Memory: %s" % total_mem)
  print("Encoded: %s" % total_encoded)
  print("Code - Memory: %s" % (total_code - total_mem))
  print("Encoded - Code: %s" % (total_encoded - total_code))
