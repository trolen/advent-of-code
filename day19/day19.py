#!/usr/bin/env python3

import fileinput
import sys

class Replacements:
  def __init__(self, lines):
    self._parse_input(lines)

  def _parse_input(self, lines):
    self._replacements = []
    self._molecule = ''
    for line in lines:
      if len(line) == 0:
        continue
      words = line.split(' => ')
      if len(words) > 1:
        self._replacements.append([words[0], words[1]])
      else:
        self._molecule = words[0]

  def run(self):
    molecules = []
    for repl in self._replacements:
      n = self._molecule.count(repl[0])
      p = 0
      while n > 0:
        p = self._molecule.find(repl[0], p)
        s = self._molecule[:p]
        s += self._molecule[p:].replace(repl[0], repl[1], 1)
        if s not in molecules:
          molecules.append(s)
        n -= 1
        p += 1
    return len(molecules)
        

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  repl = Replacements(lines)
  print(repl.run())
