#!/usr/bin/env python3

import day18
import unittest

class TestDay18(unittest.TestCase):
  def test_lights(self):
    lines = ['.#.#.#',
             '...##.',
             '#....#',
             '..#...',
             '#.#..#',
             '####..']
    lights = day18.animate_lights(lines, 4, False)
    self.assertEqual(day18.count_lights_on(lights), 4)

  def test_corners(self):
    lines = ['##.#.#',
             '...##.',
             '#....#',
             '..#...',
             '#.#..#',
             '####.#']
    lights = day18.animate_lights(lines, 5, True)
    self.assertEqual(day18.count_lights_on(lights), 17)
             
if __name__ == '__main__':
  unittest.main()
