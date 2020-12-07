#! /usr/bin/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.entries = [1721, 979, 366, 299, 675, 1456]

    def test_part1(self):
        self.assertEqual(514579, day01.do_part1(self.entries))

    def test_part2(self):
        self.assertEqual(241861950, day01.do_part2(self.entries))

if __name__ == '__main__':
    unittest.main()