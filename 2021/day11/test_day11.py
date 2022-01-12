#! /usr/bin/env python3

import unittest
import day11


class TestDay11(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '5483143223',
            '2745854711',
            '5264556173',
            '6141336146',
            '6357385478',
            '4167524645',
            '2176841721',
            '6882881134',
            '4846848554',
            '5283751526'
        ]

    def test_part1(self):
        self.assertEqual(1656, day11.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(195, day11.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
