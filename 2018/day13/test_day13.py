#! /usr/env python3

import day13
import unittest


class TestDay13(unittest.TestCase):
    def test_part1(self):
        raw_data = [
            '/->-\\',
            '|   |  /----\\',
            '| /-+--+-\\  |',
            '| | |  | v  |',
            '\\-+-/  \\-+--/',
            '  \\------/'
        ]
        app = day13.Application(raw_data)
        self.assertEqual((7, 3), app.do_part1())

    def test_part2(self):
        raw_data = [
            '/>-<\\',
            '|   |',
            '| /<+-\\',
            '| | | v',
            '\\>+</ |',
            '  |   ^',
            '  \\<->/'
        ]
        app = day13.Application(raw_data)
        self.assertEqual((6, 4), app.do_part2())


if __name__ == '__main__':
    unittest.main()
