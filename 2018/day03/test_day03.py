#! /usr/env python3

import day03
import unittest


class TestDay03(unittest.TestCase):
    def setUp(self):
        self._raw_data = [
            '# 1 @ 1,3: 4x4',
            '# 2 @ 3,1: 4x4',
            '# 3 @ 5,5: 2x2'
        ]
        self._data = day03.parse_data_lines(self._raw_data)
        self._grid = day03.build_grid(self._data)

    def test_part1(self):
        cnt = day03.count_overlap(self._grid)
        self.assertEqual(4, cnt)

    def test_part2(self):
        non_overlap = day03.find_non_overlap(self._data, self._grid)
        self.assertEqual(3, non_overlap)


if __name__ == '__main__':
    unittest.main()