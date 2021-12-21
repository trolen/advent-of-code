#! /usr/bin/env python3

import unittest
import day02


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.commands = [
            ['forward', 5],
            ['down', 5],
            ['forward', 8],
            ['up', 3],
            ['down', 8],
            ['forward', 2]
        ]

    def test_part1(self):
        self.assertEqual(150, day02.do_part1(self.commands))

    def test_part2(self):
        self.assertEqual(900, day02.do_part2(self.commands))

if __name__ == '__main__':
    unittest.main()