#!/usr/bin/env python3

import fileinput

def calc_area(l, w, h):
  return 3 * l * w + 2 * w * h + 2 * l * h

def calc_length(l, w, h):
  return 2 * l + 2 * w + l * w * h

def get_dimensions(line):
  return sorted([int(n) for n in line.split('x')])

if __name__ == "__main__":
  total_area = 0
  total_length = 0
  for line in fileinput.input():
    dims = get_dimensions(line)
    total_area += calc_area(dims[0], dims[1], dims[2])
    total_length += calc_length(dims[0], dims[1], dims[2])
  print("Total paper area: %s square feet" % total_area)
  print("Total ribbon length: %s feet" % total_length)
