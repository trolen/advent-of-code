#! /usr/bin/env python3

import unittest
import day05

class TestDay05(unittest.TestCase):
    def setUp(self):
        data = [0, 3, 0, 1, -3]
        self._maze = day05.Maze(data)

    def test_part1(self):
        self.assertEqual(5, self._maze.escape())

    def test_part2(self):
        self.assertEqual(10, self._maze.escape(part2=True))

if __name__ == '__main__':
    unittest.main()
