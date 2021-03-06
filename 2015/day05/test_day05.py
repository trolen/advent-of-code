#!/usr/bin/env python3

import day05
import unittest

class TestDay5(unittest.TestCase):
  def test_nice1(self):
    self.assertTrue(day05.is_nice1('ugknbfddgicrmopn'))
    self.assertTrue(day05.is_nice1('aaa'))
    self.assertFalse(day05.is_nice1('jchzalrnumimnmhp'))
    self.assertFalse(day05.is_nice1('haegwjzuvuyypxyu'))
    self.assertFalse(day05.is_nice1('dvszwmarrgswjxmb'))

  def test_nice2(self):
    self.assertTrue(day05.is_nice2('qjhvhtzxzqqjkmpb'))
    self.assertTrue(day05.is_nice2('xxyxx'))
    self.assertFalse(day05.is_nice2('uurcxstgmygtbstg'))
    self.assertFalse(day05.is_nice2('ieodomkazucvgmuy'))

if __name__ == '__main__':
  unittest.main()
