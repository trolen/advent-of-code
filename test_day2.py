#!/usr/bin/env python

import day2
import unittest

class TestDay2(unittest.TestCase):
  def test_area(self):
    self.assertEqual(day2.calc_area(2,3,4), 58)
    self.assertEqual(day2.calc_area(1,1,10), 43)

  def test_length(self):
    self.assertEqual(day2.calc_length(2,3,4), 34)
    self.assertEqual(day2.calc_length(1,1,10), 14)

  def test_dimensions(self):
    self.assertEqual(day2.get_dimensions('2x3x4'), [2,3,4])
    self.assertEqual(day2.get_dimensions('1x1x10'), [1,1,10])
    self.assertEqual(day2.get_dimensions('10x1x1'), [1,1,10])

if __name__ == '__main__':
  unittest.main()
