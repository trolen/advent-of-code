#! /usr/bin/env python3

import unittest
import day22


class TestDay22(unittest.TestCase):
    def setUp(self):
        raw_data = [
            'Player 1:',
            '9',
            '2',
            '6',
            '3',
            '1',
            '',
            'Player 2:',
            '5',
            '8',
            '4',
            '7',
            '10'
        ]
        self.app = day22.Application(raw_data)

    def test_part1(self):
        self.assertEqual(306, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(291, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
