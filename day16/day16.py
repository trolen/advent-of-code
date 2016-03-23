#!/usr/bin/env python3

import fileinput
import sys
import re

class Aunts:
  def __init__(self, lines):
    self._aunts = self._parse_lines(lines)

  def _parse_lines(self, lines):
    aunts = []
    pattern = re.compile(r'(?P<name>Sue \d+): (?P<p1>[a-z]+): (?P<v1>\d+), (?P<p2>[a-z]+): (?P<v2>\d+), (?P<p3>[a-z]+): (?P<v3>\d+)')
    for line in lines:
      aunt = {}
      m = pattern.match(line)
      aunt["name"] = m.group('name')
      aunt[m.group('p1')] = int(m.group('v1'))
      aunt[m.group('p2')] = int(m.group('v2'))
      aunt[m.group('p3')] = int(m.group('v3'))
      aunts.append(aunt)
    return aunts

  def analyze_ticker1(self, ticker):
    max_tally = 0
    aunt_found = ''
    for aunt in self._aunts:
      tally = 0
      for key in ticker.keys():
        if key in aunt.keys() and aunt[key] == ticker[key]:
          tally += 1
      if tally > max_tally:
        max_tally = tally
        aunt_found = aunt['name']
    return aunt_found

  def analyze_ticker2(self, ticker):
    max_tally = 0
    aunt_found = ''
    for aunt in self._aunts:
      tally = 0
      for key in ticker.keys():
        if key in aunt.keys():
          if key in ['cats', 'trees']:
            if aunt[key] > ticker[key]:
              tally += 1
          elif key in ['pomeranians', 'goldfish']:
            if aunt[key] < ticker[key]:
              tally += 1
          elif aunt[key] == ticker[key]:
            tally += 1
      if tally > max_tally:
        max_tally = tally
        aunt_found = aunt['name']
    return aunt_found

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  aunts = Aunts(lines)
  ticker = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
            'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
            'cars': 2, 'perfumes': 1}
  print("Found #1: %s" % (aunts.analyze_ticker1(ticker)))
  print("Found #2: %s" % (aunts.analyze_ticker2(ticker)))
