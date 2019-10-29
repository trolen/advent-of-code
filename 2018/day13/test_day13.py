#! /usr/env python3

import day13
import unittest


class TestDay13(unittest.TestCase):
    def test_part1(self):
        data = [
            '/->-\\',
            '|   |  /----\\',
            '| /-+--+-\\  |',
            '| | |  | v  |',
            '\\-+-/  \\-+--/',
            '  \\------/'
        ]
        (x,y) = day13.move_until_crash(data)
        self.assertEqual((7,3), (x,y))

    def test_part2(self):
        data = [
            '/>-<\\',
            '|   |',
            '| /<+-\\',
            '| | | v',
            '\\>+</ |',
            '  |   ^',
            '  \\<->/'
        ]
        (x,y) = day13.move_until_one_cart_left(data)
        self.assertEqual((6,4), (x,y))


if __name__ == '__main__':
    unittest.main()
