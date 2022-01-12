#! /usr/bin/env python3

import unittest
import day03


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.data = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ]

    def test_part1(self):
        self.assertEqual(198, day03.do_part1(self.data))

    def test_part2(self):
        self.assertEqual(230, day03.do_part2(self.data))

if __name__ == '__main__':
    unittest.main()