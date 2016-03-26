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

  def _replacement(self, molecule):
    molecules = []
    for repl in self._replacements:
      n = molecule.count(repl[0])
      p = 0
      while n > 0:
        p = molecule.find(repl[0], p)
        s = molecule[:p]
        s += molecule[p:].replace(repl[0], repl[1], 1)
        molecules.append(s)
        n -= 1
        p += len(repl[0])
    return list(set(molecules))

  def calibrate(self, molecule):
    return len(self._replacement(molecule))

  def fabricate(self, result):
    count = 1
    molecules = self._replacement('e')
    while len(molecules) > 0 and result not in molecules:
      new_molecules = []
      for molecule in molecules:
        new_molecules += self._replacement(molecule)
      for molecule in new_molecules:
        if len(molecule) > len(result):
          new_molecules.remove(molecule)
      molecules = list(set(new_molecules))
      count += 1
      print(count, len(molecules))
    return count
        
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
