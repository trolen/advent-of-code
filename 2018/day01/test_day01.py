#! /usr/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    def test_part1(self):
        final = day01.calc_frequecy_changes([+1, +1, +1])
        self.assertEqual(3, final)
        final = day01.calc_frequecy_changes([+1, +1, -2])
        self.assertEqual(0, final)
        final = day01.calc_frequecy_changes([-1, -2, -3])
        self.assertEqual(-6, final)

    def test_part2(self):
        repeat = day01.calc_frequecy_changes([+1, -1], part2=True)
        self.assertEqual(0, repeat)
        repeat = day01.calc_frequecy_changes([+3, +3, +4, -2, -4], part2=True)
        self.assertEqual(10, repeat)
        repeat = day01.calc_frequecy_changes([-6, +3, +8, +5, -6], part2=True)
        self.assertEqual(5, repeat)
        repeat = day01.calc_frequecy_changes([+7, +7, -2, -7, -4], part2=True)
        self.assertEqual(14, repeat)


if __name__ == '__main__':
    unittest.main()