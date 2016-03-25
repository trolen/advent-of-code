#!/usr/bin/env python3

import day19
import unittest

class TestDay19(unittest.TestCase):
  def test_replacements(self):
    lines = ['H => HO',
             'H => OH',
             'O => HH',
             'HOH']
    repl = day19.Replacements(lines)
    self.assertEqual(repl.run(), 4)

if __name__ == '__main__':
  unittest.main()
