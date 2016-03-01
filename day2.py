#!/usr/bin/python

INPUT_FILE="day2_input.txt"

def calc_area(l, w, h):
  return 3 * l * w + 2 * w * h + 2 * l * h

def calc_length(l, w, h):
  return 2 * l + 2 * w + l * w * h

def main():
  total_area = 0
  total_ribbon = 0
  with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
      dims = [int (n) for n in line.rstrip().split('x')]
      dims.sort()
      area = calc_area(dims[0], dims[1], dims[2])
      total_area += area
      ribbon = calc_length(dims[0], dims[1], dims[2])
      total_ribbon += ribbon
  print "Total Area:", total_area, "square feet"
  print "Total Ribbon:", total_ribbon, "feet"

if __name__ == "__main__":
  main()
