#! /usr/env python3

import unittest
import day01

class TestDay01(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(3, day01.sum_pairs('1122'))
        self.assertEqual(4, day01.sum_pairs('1111'))
        self.assertEqual(0, day01.sum_pairs('1234'))
        self.assertEqual(9, day01.sum_pairs('91212129'))

    def test_part2(self):
        self.assertEqual(6, day01.sum_pairs('1212', True))
        self.assertEqual(0, day01.sum_pairs('1221', True))
        self.assertEqual(4, day01.sum_pairs('123425', True))
        self.assertEqual(12, day01.sum_pairs('123123', True))
        self.assertEqual(4, day01.sum_pairs('12131415', True))

if __name__ == '__main__':
    unittest.main()
