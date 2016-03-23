#!/usr/bin/env python3

import day10
import unittest

class TestDay10(unittest.TestCase):
  def test_say(self):
    self.assertEqual(day10.looksay('1'), '11')
    self.assertEqual(day10.looksay('11'), '21')
    self.assertEqual(day10.looksay('21'), '1211')
    self.assertEqual(day10.looksay('1211'), '111221')
    self.assertEqual(day10.looksay('111221'), '312211')

if __name__ == '__main__':
  unittest.main()
