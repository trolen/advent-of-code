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
      n = len(repl[0])
      p = molecule.find(repl[0])
      while p >= 0:
        molecules.append(molecule[:p] + molecule[p:].replace(repl[0], repl[1], 1))
        p = molecule.find(repl[0], p + n)
    return list(set(molecules))

  def calibrate(self, molecule):
    return len(self._replacement(molecule))

  def _fabricate_impl(self, molecule, result):
    counts = []
    for m in self._replacement(molecule):
      if m == result:
        counts.append(1)
      if len(m) <= len(result):
        counts.append(1 + self._fabricate_impl(m, result))
    if len(counts) <= 0:
      return 0
    return min(counts)

  def fabricate(self, result):
    return self._fabricate_impl('e', result)

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
