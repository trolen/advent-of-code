#!/usr/bin/env python3

import day13
import unittest

class TestDay13(unittest.TestCase):
  def test_happiness(self):
    lines = ['Alice would gain 54 happiness units by sitting next to Bob.',
             'Alice would lose 79 happiness units by sitting next to Carol.',
             'Alice would lose 2 happiness units by sitting next to David.',
             'Bob would gain 83 happiness units by sitting next to Alice.',
             'Bob would lose 7 happiness units by sitting next to Carol.',
             'Bob would lose 63 happiness units by sitting next to David.',
             'Carol would lose 62 happiness units by sitting next to Alice.',
             'Carol would gain 60 happiness units by sitting next to Bob.',
             'Carol would gain 55 happiness units by sitting next to David.',
             'David would gain 46 happiness units by sitting next to Alice.',
             'David would lose 7 happiness units by sitting next to Bob.',
             'David would gain 41 happiness units by sitting next to Carol.']
    day13.parse_input(lines)
    self.assertEqual(day13.calc_happiness(), 330)

if __name__ == '__main__':
  unittest.main()
