#! /usr/env python3

import unittest
import day04


class TestDay04(unittest.TestCase):
    def test_part1(self):
        self.assertTrue(day04.is_valid_pw(111111))
        self.assertFalse(day04.is_valid_pw(223450))
        self.assertFalse(day04.is_valid_pw(123789))

    def test_part2(self):
        self.assertTrue(day04.is_valid_pw(112233, no_triples=True))
        self.assertFalse(day04.is_valid_pw(123444, no_triples=True))
        self.assertTrue(day04.is_valid_pw(111122, no_triples=True))


if __name__ == '__main__':
    unittest.main()