#! /usr/bin/env python3

import unittest
import day20

class TestDay20(unittest.TestCase):
    def setUp(self):
        data = ['5-8', '0-2', '4-7']
        self._firewall = day20.Firewall(data, 9)

    def test_part1(self):
        self.assertEqual(3, self._firewall.find_first_available())

    def test_part2(self):
        self.assertEqual(2, self._firewall.count_available())


if __name__ == '__main__':
    unittest.main()
