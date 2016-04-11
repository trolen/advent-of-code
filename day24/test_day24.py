#!/usr/bin/env python3

import day24
import unittest

class TestDay24(unittest.TestCase):
  def setUp(self):
    weights = [11, 10, 9, 8, 7, 5, 4, 3, 2, 1]
    self.packages = day24.Packages(weights)

  def test_part1(self):
    self.packages.build_groups(3)
    result = self.packages.find_shortest()
    self.assertEqual(result.quantum_entanglement, 99)

  def test_part2(self):
    self.packages.build_groups(4)
    result = self.packages.find_shortest()
    self.assertEqual(result.quantum_entanglement, 44)

if __name__ == '__main__':
  unittest.main()
