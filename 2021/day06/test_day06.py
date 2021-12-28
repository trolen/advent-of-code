#! /usr/bin/env python3

import unittest
import day06


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '3,4,3,1,2'
        ]

    def test_part1(self):
        self.assertEqual(5934, day06.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(26984457539, day06.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
