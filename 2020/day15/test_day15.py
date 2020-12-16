#! /usr/bin/env python3

import unittest
import day15


class TestDay15(unittest.TestCase):
    def setUp(self):
        raw_data = [
            '0,3,6'
        ]
        self.app = day15.Application(raw_data)

    def test_part1(self):
        self.assertEqual(436, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(175594, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
