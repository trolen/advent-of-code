#! /usr/bin/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_part1(self):
        entries = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(514579, day01.do_part1(entries))

    def test_part2(self):
        entries = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(241861950, day01.do_part2(entries))

if __name__ == '__main__':
    unittest.main()