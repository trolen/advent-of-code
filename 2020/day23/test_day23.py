#! /usr/bin/env python3

import unittest
import day23


class TestDay23(unittest.TestCase):
    def setUp(self):
        raw_data = [
            '389125467'
        ]
        self.app = day23.Application(raw_data)

    def test_part1(self):
        self.assertEqual('67384529', self.app.do_part1())

    def test_part2(self):
        self.assertEqual(149245887792, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
