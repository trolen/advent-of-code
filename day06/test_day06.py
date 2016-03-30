#!/usr/bin/env python3

import day06
import unittest

class TestDay6(unittest.TestCase):
  def test_parse_line(self):
    cmd = day06.parse_line('turn on 0,0 through 999,999')
    self.assertEqual(type(cmd), day06.TurnOn)
    self.assertEqual(cmd.range[0], (0, 0))
    self.assertEqual(cmd.range[1], (999, 999))
    cmd = day06.parse_line('toggle 50,50 through 100,100')
    self.assertEqual(type(cmd), day06.Toggle)
    self.assertEqual(cmd.range[0], (50, 50))
    self.assertEqual(cmd.range[1], (100, 100))

  def test_part1(self):
    lights = day06.make_grid()
    cmd = day06.parse_line('turn on 0,0 through 999,999')
    cmd.part1(lights)
    self.assertEqual(day06.grid_sum(lights), 1000000)
    cmd = day06.parse_line('turn off 0,0 through 499,499')
    cmd.part1(lights)
    self.assertEqual(day06.grid_sum(lights), 750000)

  def test_part2(self):
    lights = day06.make_grid()
    cmd = day06.parse_line('turn on 0,0 through 0,0')
    cmd.part2(lights)
    self.assertEqual(day06.grid_sum(lights), 1)
    cmd = day06.parse_line('toggle 0,0 through 999,999')
    cmd.part2(lights)
    self.assertEqual(day06.grid_sum(lights), 2000001)

if __name__ == '__main__':
  unittest.main()
