#!/usr/bin/env python3

import day4
import unittest

class TestDay4(unittest.TestCase):
  def test_find_hash(self):
    self.assertEqual(day4.find_hash('abcdef', '00000'), 609043)
    self.assertEqual(day4.find_hash('pqrstuv', '00000'), 1048970)

if __name__ == '__main__':
  unittest.main()
