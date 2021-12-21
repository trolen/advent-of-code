#! /usr/bin/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part1(self):
        self.assertEqual(7, day01.do_part1(self.depths))

    def test_part2(self):
        self.assertEqual(5, day01.do_part2(self.depths))

if __name__ == '__main__':
    unittest.main()