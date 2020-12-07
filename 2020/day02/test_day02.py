#! /usr/bin/env python3

import unittest
import day02


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.raw_data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
        self.pwd_entries = day02.parse_data(self.raw_data)

    def test_part1(self):
        self.assertEqual(2, day02.do_part1(self.pwd_entries))

    def test_part2(self):
        self.assertEqual(1, day02.do_part2(self.pwd_entries))


if __name__ == '__main__':
    unittest.main()
