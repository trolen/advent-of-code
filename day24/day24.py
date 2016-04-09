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
    self._num_groups = 3
    self._calc_group_weight()

  def _calc_group_weight(self):
    n = sum(self._weights)
    if n % self._num_groups != 0:
      print("Error calculating group weight: Not evenly divisible by %s" % self._num_groups)
      sys.exit(1)
    self._group_weight = int(n / self._num_groups)

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

  def build_groups(self):
    self._groups = []
    for g in self._find_groups(self._weights, self._group_weight):
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
  packages.build_groups()
  result = packages.find_shortest()
  print("Quantum Entanglement (part 1): %s" % result.quantum_entanglement)
