#!/usr/bin/env python3

import fileinput
import sys

class Group:
  def __init__(self, weights):
    self.weights = weights
    self.count = len(weights)
    self.quantum_entanglement = self._calc_qe(weights)

  def _calc_qe(self, weights):
    result = 1
    for w in weights:
      result *= w
    return result

class Packages:
  def __init__(self, weights):
    self._weights = sorted(weights, reverse=True)

  def _calc_group_weight(self, n_groups):
    n = sum(self._weights)
    if n % n_groups != 0:
      print("Error calculating group weight: Not evenly divisible by %s" % n_groups)
      sys.exit(1)
    return int(n / n_groups)

  def _find_groups(self, weights, group_wt):
    n = len(weights)
    groups = []
    for i in range(n):
      if weights[i] == group_wt:
        groups.append([weights[i]])
      if weights[i] >= group_wt:
        continue
      s = sum(weights[i:])
      if s == group_wt:
        groups.append(weights[i:])
      if s <= group_wt:
        break
      for g in self._find_groups(weights[i+1:], group_wt - weights[i]):
        groups.append([weights[i]] + g)
    return groups

  def build_groups(self, n_groups):
    group_wt = self._calc_group_weight(n_groups)
    self._groups = []
    for g in self._find_groups(self._weights, group_wt):
      self._groups.append(Group(g))

  def find_shortest(self):
    result = self._groups[0]
    for g in self._groups[1:]:
      if g.count > result.count:
        continue
      if g.count < result.count:
        result = g
      if g.quantum_entanglement < result.quantum_entanglement:
        result = g
    return result

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [int(line.rstrip()) for line in fileinput.input()]

if __name__ == "__main__":
  packages = Packages(read_input())
  packages.build_groups(3)
  result = packages.find_shortest()
  print("Quantum Entanglement (part 1): %s" % result.quantum_entanglement)
  packages.build_groups(4)
  result = packages.find_shortest()
  print("Quantum Entanglement (part 2): %s" % result.quantum_entanglement)
