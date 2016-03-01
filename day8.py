#!/usr/bin/python

INPUT_FILE="day8_input.txt"

def encode(s):
  result = '"'
  for c in s:
    if c in '"\\':
      result += '\\'
    result += c
  result += '"'
  return result

def accumulate_totals():
  total_code = 0
  total_mem = 0
  total_encoded = 0
  with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.rstrip()
      total_code += len(line)
      total_mem += len(eval(line))
      total_encoded += len(encode(line))
  return (total_code, total_mem, total_encoded)

if __name__ == "__main__":
  (code, mem, encoded) = accumulate_totals()
  print "Code:", code
  print "Memory:", mem
  print "Encoded:", encoded
  print "Code - Memory:", code - mem
  print "Encoded - Code:", encoded - code
