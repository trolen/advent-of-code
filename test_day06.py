#!/usr/bin/env python3

import day06
import unittest

class TestDay6(unittest.TestCase):
  def test_parse_line(self):
    self.assertEqual(day06.parse_line('turn on 0,0 through 999,999'),
      ('turn on', 0, 0, 999, 999))
    self.assertEqual(day06.parse_line('toggle 249,249 through 250,250'),
      ('toggle', 249, 249, 250, 250))
    self.assertEqual(day06.parse_line('turn off 250,250 through 749,749'),
      ('turn off', 250, 250, 749, 749))

  def test_set_lights1(self):
    self.assertEqual(day06.set_lights1(['turn on 0,0 through 999,999']), 1000000)
    self.assertEqual(day06.set_lights1(['turn on 0,0 through 999,999',
      'toggle 0,0 through 999,0']), 999000)
    self.assertEqual(day06.set_lights1(['turn on 0,0 through 499,499',
      'toggle 249,249 through 250,250']), 249996)
    self.assertEqual(day06.set_lights1(['turn on 0,0 through 99,99',
      'turn off 25,25 through 74,74']), 7500)

  def test_set_lights2(self):
    self.assertEqual(day06.set_lights2(['turn on 0,0 through 0,0']), 1)
    self.assertEqual(day06.set_lights2(['toggle 0,0 through 999,999']), 2000000)

if __name__ == '__main__':
  unittest.main()
