#!/usr/bin/env python3

def get_sequence(row, col):
  diagonal = row + col - 1
  result = 1
  for i in range(1, diagonal):
    result += i
  result += col - 1
  return result

def calc_code(row, col):
  seq_no = get_sequence(row, col)
  code = 20151125
  for i in range(seq_no - 1):
    code *= 252533
    code %= 33554393
  return code

if __name__ == "__main__":
  r = 3010
  c = 3019
  code = calc_code(r, c)
  print("Code at (%s, %s): %s" % (r, c, code))
