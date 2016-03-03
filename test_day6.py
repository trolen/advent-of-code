#!/usr/bin/env python3

import day6
import unittest

class TestDay5(unittest.TestCase):
  def test_set_lights1(self):
    self.assertEqual(day6.set_lights1(['turn on 0,0 through 999,999']), 1000000)

if __name__ == '__main__':
  unittest.main()
