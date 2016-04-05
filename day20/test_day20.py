#!/usr/bin/env python3

import day20
import unittest

class TestDay20(unittest.TestCase):
  def test_factors(self):
    self.assertEqual(day20.factors(100), [1, 2, 4, 5, 10, 20, 25, 50, 100])

  def test_presents1(self):
    self.assertEqual(day20.presents(1, 1), 10)
    self.assertEqual(day20.presents(2, 1), 30)
    self.assertEqual(day20.presents(3, 1), 40)
    self.assertEqual(day20.presents(4, 1), 70)
    self.assertEqual(day20.presents(5, 1), 60)
    self.assertEqual(day20.presents(6, 1), 120)
    self.assertEqual(day20.presents(7, 1), 80)
    self.assertEqual(day20.presents(8, 1), 150)
    self.assertEqual(day20.presents(9, 1), 130)

  def test_presents2(self):
    self.assertEqual(day20.presents(150, 2), 4026)

  def test_find_house1(self):
    self.assertEqual(day20.find_house(100, 1), 6)
    self.assertEqual(day20.find_house(150, 1), 8)

if __name__ == '__main__':
  unittest.main()
