#! /usr/bin/env python3

import unittest
import day12

class TestDay12(unittest.TestCase):
    def setUp(self):
        data = [
            '0 <-> 2',
            '1 <-> 1',
            '2 <-> 0, 3, 4',
            '3 <-> 2, 4',
            '4 <-> 2, 3, 6',
            '5 <-> 6',
            '6 <-> 4, 5'
        ]
        self._pipes = day12.Pipes(data)

    def test_part1(self):
        self.assertEqual(6, len(self._pipes.traverse_pipes('0')))

    def test_part2(self):
        self.assertEqual(2, self._pipes.count_groups())


if __name__ == '__main__':
    unittest.main()
