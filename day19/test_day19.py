#!/usr/bin/env python3

import day19
import unittest

class TestDay19(unittest.TestCase):
  def test_calibration(self):
    lines = ['H => HO',
             'H => OH',
             'O => HH']
    molecules = day19.Molecules(lines)
    self.assertEqual(molecules.calibrate('HOH'), 4)

  def test_fabrication(self):
    lines = ['e => H',
             'e => O',
             'H => HO',
             'H => OH',
             'O => HH']
    molecules = day19.Molecules(lines)
    self.assertEqual(molecules.fabricate('HOH'), 3)
    self.assertEqual(molecules.fabricate('HOHOHO'), 6)

if __name__ == '__main__':
  unittest.main()
