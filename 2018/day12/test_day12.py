#! /usr/env python3

import day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self):
        self._data = [
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

    def test_part1(self):
        n = day12.calc_score_after_generations(self._data, 20)
        self.assertEqual(325, n)


if __name__ == '__main__':
    unittest.main()
