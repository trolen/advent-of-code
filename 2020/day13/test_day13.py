#! /usr/bin/env python3

import unittest
import day13


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.app = day13.Application([
            '939',
            '7,13,x,x,59,x,31,19'
        ])

    def test_part1(self):
        self.assertEqual(295, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(1068781, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
