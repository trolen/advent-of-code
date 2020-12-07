#! /usr/bin/env python3

import unittest
import day03


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#'
        ]

    def test_part1(self):
        self.assertEqual(7, day03.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(336, day03.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
