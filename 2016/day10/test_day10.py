#! /usr/bin/env python3

import unittest
import day10

class TestDay10(unittest.TestCase):
    def setUp(self):
        self._instructions = [
            'value 5 goes to bot 2',
            'bot 2 gives low to bot 1 and high to bot 0',
            'value 3 goes to bot 1',
            'bot 1 gives low to output 1 and high to bot 0',
            'bot 0 gives low to output 2 and high to output 0',
            'value 2 goes to bot 2'
        ]
        self._balance_bots = day10.BalanceBots(self._instructions)

    def test_part1(self):
        self.assertEqual(self._balance_bots.run_part1(2, 5), '2')

    def test_part2(self):
        self.assertEqual(self._balance_bots.run_part2(), 30)


if __name__ == '__main__':
    unittest.main()
