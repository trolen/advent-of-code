#!/usr/bin/python

INPUT_FILE="day5_input.txt"
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

def count_nice_strings(ver):
  nice_count = 0
  with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.rstrip()
      if ver == 1 and is_nice1(line):
        nice_count += 1
      if ver == 2 and is_nice2(line):
        nice_count += 1
  return nice_count

if __name__ == "__main__":
  print "Nice strings #1:", count_nice_strings(1)
  print "Nice strings #2:", count_nice_strings(2)
