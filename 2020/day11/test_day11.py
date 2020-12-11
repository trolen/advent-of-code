#! /usr/bin/env python3

import unittest
import day11


class TestDay11(unittest.TestCase):
    def setUp(self):
        pass
        self.app = day11.Application([
            'L.LL.LL.LL',
            'LLLLLLL.LL',
            'L.L.L..L..',
            'LLLL.LL.LL',
            'L.LL.LL.LL',
            'L.LLLLL.LL',
            '..L.L.....',
            'LLLLLLLLLL',
            'L.LLLLLL.L',
            'L.LLLLL.LL'
        ])

    def test_part1(self):
        self.assertEqual(37, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(26, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
