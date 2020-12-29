#! /usr/bin/env python3

import unittest
import day17


class TestDay17(unittest.TestCase):
    def setUp(self):
        raw_data = [
            '.#.',
            '..#',
            '###'
        ]
        self.app = day17.Application(raw_data)

    def test_part1(self):
        self.assertEqual(112, self.app.do_part1())

    def test_part2(self):
        pass
        #self.assertEqual(848, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
