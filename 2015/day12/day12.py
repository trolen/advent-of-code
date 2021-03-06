#!/usr/bin/env python3

import fileinput
import json
import sys

def calc_sum(obj, ignore_red):
  if type(obj) is int:
    return obj
  if type(obj) is str:
    return 0
  total = 0
  if type(obj) is list:
    for x in obj:
      total += calc_sum(x, ignore_red)
    return total
  if type(obj) is dict:
    if ignore_red:
      for k in obj.keys():
        if obj[k] == "red":
          return 0
    for k in obj.keys():
      total += calc_sum(obj[k], ignore_red)
    return total
  return total

def sum_of_ints(data, ignore_red):
  obj = json.loads(data)
  return calc_sum(obj, ignore_red)

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return ''.join([line.rstrip() for line in fileinput.input()])

if __name__ == "__main__":
  data = read_input()
  print("Sum: %s" % sum_of_ints(data, False))
  print("Sum (ignoring red objects): %s" % sum_of_ints(data, True))
