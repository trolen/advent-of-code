#! /usr/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(2, day01.fuel_required(12))
        self.assertEqual(2, day01.fuel_required(14))
        self.assertEqual(654, day01.fuel_required(1969))
        self.assertEqual(33583, day01.fuel_required(100756))

    def test_part2(self):
        self.assertEqual(2, day01.fuel_required2(14))
        self.assertEqual(966, day01.fuel_required2(1969))
        self.assertEqual(50346, day01.fuel_required2(100756))


if __name__ == '__main__':
    unittest.main()