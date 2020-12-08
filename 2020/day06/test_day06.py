#! /usr/bin/env python3

import unittest
import day06


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'abc',
            '',
            'a',
            'b',
            'c',
            '',
            'ab',
            'ac',
            '',
            'a',
            'a',
            'a',
            'a',
            '',
            'b'
        ]
        self.groups = day06.parse_data(self.raw_data)

    def test_unique_chars(self):
        self.assertEqual('abc', day06.get_unique_chars(['ab', 'ac']))

    def test_common_chars(self):
        self.assertEqual('a', day06.get_common_chars(['ab', 'ac']))

    def test_part1(self):
        self.assertEqual(11, day06.do_part1(self.groups))

    def test_part2(self):
        self.assertEqual(6, day06.do_part2(self.groups))


if __name__ == '__main__':
    unittest.main()
