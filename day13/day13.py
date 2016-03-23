#!/usr/bin/env python3

import fileinput
import itertools
import sys

guests = []
happiness = []

def parse_input(lines):
  global guests
  global happiness
  for line in lines:
    words = line.split(' ')
    if not words[0] in guests:
      guests.append(words[0])
    sign = 1 if words[2] == 'gain' else -1
    happiness.append([words[0], words[-1][:-1], sign * int(words[3])])

def find_happiness(g1, g2):
  global happiness
  for h in happiness:
    if h[0] == g1 and h[1] == g2:
      return h[2]
  return None

def calc_happiness():
  global guests
  perms = list(itertools.permutations(guests))
  results = []
  for p in perms:
    h = 0
    l = len(p)
    for i in range(l):
      h += find_happiness(p[i], p[i - 1])
      if i < l - 1:
        h += find_happiness(p[i], p[i + 1])
      else:
        h += find_happiness(p[i], p[0])
    results.append(h)
  results.sort()
  return results[-1]

def add_me():
  global guests
  global happiness
  for g in guests:
    happiness.append(["Me", g, 0])
    happiness.append([g, "Me", 0])
  guests.append("Me")

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  parse_input(lines)
  print("Happiness: %s" % calc_happiness())
  add_me()
  print("Happiness (with me): %s" % calc_happiness())
