#! /usr/env python3

import day05
import unittest


class TestDay05(unittest.TestCase):
    def setUp(self):
        self._data = 'dabAcCaCBAcCcaDA'

    def test_part1(self):
        s = day05.process_reactions(self._data)
        self.assertEqual('dabCBAcaDA', s)

    def test_part2(self):
        s = day05.find_shortest_polymer(self._data)
        self.assertEqual('daDA', s)


if __name__ == '__main__':
    unittest.main()