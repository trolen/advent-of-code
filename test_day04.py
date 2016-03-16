#!/usr/bin/env python3

import day04
import unittest

class TestDay4(unittest.TestCase):
  def test_find_hash(self):
    self.assertEqual(day04.find_hash('abcdef', 5), (609043, '000001dbbfa3a5c83a2d506429c7b00e'))
    self.assertEqual(day04.find_hash('pqrstuv', 5), (1048970,'000006136ef2ff3b291c85725f17325c'))

if __name__ == '__main__':
  unittest.main()
