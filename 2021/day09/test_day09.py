#! /usr/bin/env python3

import unittest
import day09


class TestDay09(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '2199943210',
            '3987894921',
            '9856789892',
            '8767896789',
            '9899965678'
        ]

    def test_part1(self):
        self.assertEqual(15, day09.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(1134, day09.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
