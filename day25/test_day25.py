#!/usr/bin/env python3

import day25
import unittest

class TestDay25(unittest.TestCase):
  def test_sequence(self):
    self.assertEqual(day25.get_sequence(1, 1), 1)
    self.assertEqual(day25.get_sequence(4, 2), 12)
    self.assertEqual(day25.get_sequence(3, 3), 13)
    self.assertEqual(day25.get_sequence(1, 5), 15)
    self.assertEqual(day25.get_sequence(3, 4), 19)

  def test_code(self):
    self.assertEqual(day25.calc_code(1, 1), 20151125)
    self.assertEqual(day25.calc_code(4, 2), 32451966)
    self.assertEqual(day25.calc_code(1, 5), 10071777)
    self.assertEqual(day25.calc_code(3, 4), 7981243)

if __name__ == '__main__':
  unittest.main()
