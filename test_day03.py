#!/usr/bin/env python3

import day03
import unittest

class TestDay3(unittest.TestCase):
  def test_year1(self):
    self.assertEqual(day03.year1('>'), 2)
    self.assertEqual(day03.year1('^>v<'), 4)
    self.assertEqual(day03.year1('^v^v^v^v^v'), 2)

  def test_year2(self):
    self.assertEqual(day03.year2('^v'), 3)
    self.assertEqual(day03.year2('^>v<'), 3)
    self.assertEqual(day03.year2('^v^v^v^v^v'), 11)

if __name__ == '__main__':
  unittest.main()
