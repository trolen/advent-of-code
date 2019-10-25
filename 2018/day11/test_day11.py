#! /usr/env python3

import day11
import unittest


class TestDay11(unittest.TestCase):
    def test_part1(self):
        pwr = day11.calc_power_level(3, 5, 8)
        self.assertEqual(4, pwr)
        pwr = day11.calc_power_level(122, 79, 57)
        self.assertEqual(-5, pwr)
        pwr = day11.calc_power_level(217, 196, 39)
        self.assertEqual(0, pwr)
        pwr = day11.calc_power_level(101, 153, 71)
        self.assertEqual(4, pwr)
        grid = day11.build_grid(18)
        point = day11.find_largest_power_by_size(grid)
        self.assertEqual((33,45), (point[0], point[1]))
        grid = day11.build_grid(42)
        point = day11.find_largest_power_by_size(grid)
        self.assertEqual((21,61), (point[0], point[1]))

    def test_part2(self):
        grid = day11.build_grid(18)
        point = day11.find_largest_power_any_size(grid)
        self.assertEqual((90,269,16), point)
        grid = day11.build_grid(42)
        point = day11.find_largest_power_any_size(grid)
        self.assertEqual((232,251,12), point)


if __name__ == '__main__':
    unittest.main()
