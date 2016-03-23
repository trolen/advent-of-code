#!/usr/bin/env python3

import day14
import unittest

class TestDay14(unittest.TestCase):
  def test_race(self):
    lines = ['Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
             'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
    race = day14.Race(lines)
    race.run(1000)
    self.assertEqual(race.max_distance(), 1120)
    self.assertEqual(race.max_points(), 689)

if __name__ == '__main__':
  unittest.main()
