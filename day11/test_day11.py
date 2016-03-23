#!/usr/bin/env python3

import day11
import unittest

class TestDay11(unittest.TestCase):
  def test_inrement(self):
    self.assertEqual(day11.increment('abc'), 'abd')
    self.assertEqual(day11.increment('bcd'), 'bce')
    self.assertEqual(day11.increment('xyz'), 'xza')
    self.assertEqual(day11.increment('azz'), 'baa')

  def test_is_valid(self):
    self.assertFalse(day11.is_valid('hijklmmn'))
    self.assertFalse(day11.is_valid('abbceffg'))
    self.assertFalse(day11.is_valid('abbcegjk'))
    self.assertTrue(day11.is_valid('aaefghkk'))

  def test_find_next(self):
    self.assertEqual(day11.find_next('abcdefgh'), 'abcdffaa')
    self.assertEqual(day11.find_next('ghijklmn'), 'ghjaabcc')

if __name__ == '__main__':
  unittest.main()
