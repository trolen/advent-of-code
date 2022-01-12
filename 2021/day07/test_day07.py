#! /usr/bin/env python3

import unittest
import day07


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '16,1,2,0,4,2,7,1,2,14'
        ]

    def test_part1(self):
        self.assertEqual(37, day07.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(168, day07.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
