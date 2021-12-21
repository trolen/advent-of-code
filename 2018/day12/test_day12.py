#! /usr/env python3

import day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'initial state: #..#.#..##......###...###',
            '',
            '...## => #',
            '..#.. => #',
            '.#... => #',
            '.#.#. => #',
            '.#.## => #',
            '.##.. => #',
            '.#### => #',
            '#.#.# => #',
            '#.### => #',
            '##.#. => #',
            '##.## => #',
            '###.. => #',
            '###.# => #',
            '####. => #'
        ]
        self.app = day12.Application(self.raw_data)

    def test_part1(self):
        self.assertEqual(325, self.app.do_part1())


if __name__ == '__main__':
    unittest.main()
