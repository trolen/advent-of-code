#! /usr/env python3

import day06
import unittest


class TestDay06(unittest.TestCase):
    def setUp(self):
        self._data = [
            '1, 1',
            '1, 6',
            '8, 3',
            '3, 4',
            '5, 5',
            '8, 9'
        ]
        self._points = day06.parse_points(self._data)
        self._grid = day06.build_grid_with_areas(self._points)

    def test_manhattan_distance(self):
        d = day06.manhattan_distance(self._points[0], (0,0))
        self.assertEqual(2, d)
        d = day06.manhattan_distance(self._points[1], (0,0))
        self.assertEqual(7, d)
        d = day06.manhattan_distance(self._points[0], (4,3))
        self.assertEqual(5, d)
        d = day06.manhattan_distance(self._points[5], (4,3))
        self.assertEqual(10, d)

    def test_part1(self):
        a = day06.find_largest_non_infinite_area(self._points, self._grid)
        self.assertEqual(17, a)

    def test_part2(self):
        a = day06.find_area_within_distance(self._points, self._grid, 32)
        self.assertEqual(16, a)


if __name__ == '__main__':
    unittest.main()