#! /usr/bin/env python3

import unittest
import day24

class TestDay24(unittest.TestCase):
    def setUp(self):
        data = [
            '0/2',
            '2/2',
            '2/3',
            '3/4',
            '3/5',
            '0/1',
            '10/1',
            '9/10'
        ]
        self._moat = day24.Moat(data)

    def test_part1(self):
        self.assertEqual(31, self._moat.find_strongest())

    def test_part2(self):
        self.assertEqual(19, self._moat.find_longest())


if __name__ == '__main__':
    unittest.main()