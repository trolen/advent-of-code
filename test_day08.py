#!/usr/bin/env python3

import day08
import unittest

class TestDay8(unittest.TestCase):
  def test_code_length(self):
    self.assertEqual(day08.calc_code_length('""'), 2)
    self.assertEqual(day08.calc_code_length('"abc"'), 5)
    self.assertEqual(day08.calc_code_length('"aaa\\"aaa"'), 10)
    self.assertEqual(day08.calc_code_length('"\\x27"'), 6)

  def test_mem_length(self):
    self.assertEqual(day08.calc_mem_length('""'), 0)
    self.assertEqual(day08.calc_mem_length('"abc"'), 3)
    self.assertEqual(day08.calc_mem_length('"aaa\\"aaa"'), 7)
    self.assertEqual(day08.calc_mem_length('"\\x27"'), 1)

  def test_encoded_length(self):
    self.assertEqual(day08.calc_encoded_length('""'), 6)
    self.assertEqual(day08.calc_encoded_length('"abc"'), 9)
    self.assertEqual(day08.calc_encoded_length('"aaa\\"aaa"'), 16)
    self.assertEqual(day08.calc_encoded_length('"\\x27"'), 11)

if __name__ == '__main__':
  unittest.main()
