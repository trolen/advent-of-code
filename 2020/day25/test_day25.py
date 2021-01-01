#! /usr/bin/env python3

import unittest
import day25


class TestDay25(unittest.TestCase):
    def setUp(self):
        raw_data = [
            '5764801',
            '17807724'
        ]
        self.app = day25.Application(raw_data)

    def test_part1(self):
        self.assertEqual(14897079, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(0, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
