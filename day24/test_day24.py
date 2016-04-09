#!/usr/bin/env python3

import day24
import unittest

class TestDay24(unittest.TestCase):
  def setUp(self):
    weights = [11, 10, 9, 8, 7, 5, 4, 3, 2, 1]
    self.packages = day24.Packages(weights)

  def test_part1(self):
    pass

if __name__ == '__main__':
  unittest.main()
