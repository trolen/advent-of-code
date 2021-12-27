#! /usr/bin/env python3

import unittest
import day05


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '0, 9 -> 5, 9',
            '8, 0 -> 0, 8',
            '9, 4 -> 3, 4',
            '2, 2 -> 2, 1',
            '7, 0 -> 7, 4',
            '6, 4 -> 2, 0',
            '0, 9 -> 2, 9',
            '3, 4 -> 1, 4',
            '0, 0 -> 8, 8',
            '5, 5 -> 8, 2'
        ]

    def test_part1(self):
        self.assertEqual(5, day05.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(12, day05.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
