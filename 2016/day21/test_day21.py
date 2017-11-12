#! /usr/bin/env python3

import unittest
import day21

class TestDay21(unittest.TestCase):
    def setUp(self):
        instructions = [
            'swap position 4 with position 0',
            'swap letter d with letter b',
            'reverse positions 0 through 4',
            'rotate left 1 step',
            'move position 1 to position 4',
            'move position 3 to position 0',
            'rotate based on position of letter b',
            'rotate based on position of letter d'
        ]
        self._scrambler = day21.Scrambler(instructions)

    def test_scramble(self):
        self.assertEqual('decab', self._scrambler.scramble('abcde'))

    def test_unscramble(self):
        self.assertEqual('abcde', self._scrambler.unscramble('decab'))


if __name__ == '__main__':
    unittest.main()
