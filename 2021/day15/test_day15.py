#! /usr/bin/env python3

import unittest
import day15


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '1163751742',
            '1381373672',
            '2136511328',
            '3694931569',
            '7463417111',
            '1319128137',
            '1359912421',
            '3125421639',
            '1293138521',
            '2311944581'
        ]

    def test_part1(self):
        self.assertEqual(40, day15.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(315, day15.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
