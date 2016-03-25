#!/usr/bin/env python3

import fileinput
import sys

class Molecules:
  def __init__(self, lines):
    self._parse_input(lines)

  def _parse_input(self, lines):
    self._replacements = []
    for line in lines:
      if len(line) == 0:
        continue
      words = line.split(' => ')
      self._replacements.append([words[0], words[1]])

  def calibrate(self, molecule):
    molecules = []
    for repl in self._replacements:
      n = molecule.count(repl[0])
      p = 0
      while n > 0:
        p = molecule.find(repl[0], p)
        s = molecule[:p]
        s += molecule[p:].replace(repl[0], repl[1], 1)
        if s not in molecules:
          molecules.append(s)
        n -= 1
        p += 1
    return len(molecules)

  def fabricate(self, molecule):
    return 0
        
def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  molecules = Molecules(lines[:-1])
  print("Calibration: %s" % molecules.calibrate(lines[-1]))
  print("Fabricate: %s" % molecules.fabricate(lines[-1]))
