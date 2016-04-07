#!/usr/bin/env python3

import day23
import unittest

class TestDay23(unittest.TestCase):
  def test_part1(self):
    lines = ['inc a',
             'jio a, +2',
             'tpl a',
             'inc a']
    computer = day23.Computer(lines)
    computer.run()
    self.assertEqual(computer.register('a'), 2)

if __name__ == '__main__':
  unittest.main()
