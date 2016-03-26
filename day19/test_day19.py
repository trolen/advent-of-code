#!/usr/bin/env python3

import day19
import unittest

class TestDay19(unittest.TestCase):
  def setUp(self):
    self._replacements = ['e => H',
                          'e => O',
                          'H => HO',
                          'H => OH',
                          'O => HH']
    self._molecules = day19.Molecules(self._replacements)
  
  def test_calibration(self):
    self.assertEqual(self._molecules.calibrate('HOH'), 4)

  def test_fabrication(self):
    self.assertEqual(self._molecules.fabricate('HOH'), 3)
    self.assertEqual(self._molecules.fabricate('HOHOHO'), 6)

if __name__ == '__main__':
  unittest.main()
