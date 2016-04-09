#!/usr/bin/env python3

import fileinput
import sys

class Packages:
  def __init__(self, weights):
    self._weights = sorted(weights, reverse=True)
    self._num_groups = 3
    self._calc_group_weight()

  def _calc_group_weight(self):
    n = sum(self._weights)
    if n % self._num_groups != 0:
      print("Error calculating group weight: Not evenly divisible by %s" % self._num_groups)
      sys.exit(1)
    self._group_weight = n / self._num_groups

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [int(line.rstrip()) for line in fileinput.input()]

if __name__ == "__main__":
  packages = Packages(read_input())
