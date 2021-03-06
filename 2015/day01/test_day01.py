#!/usr/bin/env python3

import day01
import unittest

class TestDay1(unittest.TestCase):
  def test_zero(self):
    self.assertEqual(day01.elevator(''), 0)
    self.assertEqual(day01.elevator('(())'), 0)
    self.assertEqual(day01.elevator('()()'), 0)

  def test_upper(self):
    self.assertEqual(day01.elevator('((('), 3)
    self.assertEqual(day01.elevator('(()(()('), 3)
    self.assertEqual(day01.elevator('))((((('), 3)

  def test_lower(self):
    self.assertEqual(day01.elevator('())'), -1)
    self.assertEqual(day01.elevator('))('), -1)
    self.assertEqual(day01.elevator(')))'), -3)
    self.assertEqual(day01.elevator(')())())'), -3)

  def test_position(self):
    self.assertEqual(day01.enter_basement(''), None)
    self.assertEqual(day01.enter_basement(')'), 1)
    self.assertEqual(day01.enter_basement('()())'), 5)

if __name__ == '__main__':
  unittest.main()
