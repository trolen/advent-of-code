#! /usr/bin/env python3

import unittest
import day13


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '6,10',
            '0,14',
            '9,10',
            '0,3',
            '10,4',
            '4,11',
            '6,0',
            '6,12',
            '4,1',
            '0,13',
            '10,12',
            '3,4',
            '3,0',
            '8,4',
            '1,10',
            '2,14',
            '8,10',
            '9,0',
            '',
            'fold along y=7',
            'fold along x=5'
        ]

    def test_part1(self):
        self.assertEqual(17, day13.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(16, day13.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
