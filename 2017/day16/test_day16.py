#! /usr/bin/env python3

import unittest
import day16

class TestDay16(unittest.TestCase):
    def setUp(self):
        self._programs = day16.DancingPrograms(5, 's1,x3/4,pe/b')

    def test_part1(self):
        self.assertEqual('baedc', self._programs.dance())

    def test_part2(self):
        self.assertEqual('ceadb', self._programs.dance(2))


if __name__ == '__main__':
    unittest.main()
