#! /usr/bin/env python3

import unittest
import day13

class TestDay13(unittest.TestCase):
    def setUp(self):
        data = [
            '0: 3',
            '1: 2',
            '4: 4',
            '6: 4'
        ]
        self._firewall = day13.Firewall(data)

    def test_part1(self):
        self.assertEqual(24, self._firewall.find_severity())

    def test_part2(self):
        self.assertEqual(10, self._firewall.find_min_delay())


if __name__ == '__main__':
    unittest.main()
