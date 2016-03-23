#!/usr/bin/env python3

def increment(s):
  result = ''
  carry = 1
  ord_a = ord('a')
  for c in s[::-1]:
    new_ord = ord(c) - ord_a + carry
    result += chr(int(new_ord % 26) + ord_a)
    carry = new_ord / 26
  return result[::-1]

def is_valid(s):
  disallowed = 'ilo'
  for c in disallowed:
    if c in s:
      return False
  found_straight = False
  count_pairs = 0
  c1 = ' '
  c2 = ' '
  for c in s:
    if ord(c) == ord(c1) + 1 and ord(c1) == ord(c2) + 1:
      found_straight = True
    if c == c1 and c1 != c2:
      count_pairs += 1
    c2 = c1
    c1 = c
  return found_straight and count_pairs >= 2

def find_next(s):
  while True:
    s = increment(s)
    if is_valid(s):
      return s

if __name__ == "__main__":
  pw1 = find_next('cqjxjnds')
  print("Password #1: %s" % pw1)
  pw2 = find_next(pw1)
  print("Password #2: %s" % pw2)
