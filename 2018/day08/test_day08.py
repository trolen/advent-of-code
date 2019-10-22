#! /usr/env python3

import day08
import unittest


class TestDay08(unittest.TestCase):
    def setUp(self):
        self._data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
        self._nodes = day08.parse_nodes(self._data)

    def test_part1(self):
        n = day08.sum_metadata(self._nodes)
        self.assertEqual(138, n)

    def test_part2(self):
        n = day08.calc_value(self._nodes)
        self.assertEqual(66, n)


if __name__ == '__main__':
    unittest.main()