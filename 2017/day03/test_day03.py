#! /usr/bin/env python3

import unittest
import day03

class TestDay3(unittest.TestCase):
    def test_part1(self):
        grid = day03.MemoryGrid(1)
        self.assertEqual(0, grid.calc_distance())
        grid = day03.MemoryGrid(12)
        self.assertEqual(3, grid.calc_distance())
        grid = day03.MemoryGrid(23)
        self.assertEqual(2, grid.calc_distance())
        grid = day03.MemoryGrid(1024)
        self.assertEqual(31, grid.calc_distance())

    def test_part2(self):
        grid = day03.MemoryGrid(23)
        self.assertEqual(25, grid.part2())


if __name__ == '__main__':
    unittest.main()
