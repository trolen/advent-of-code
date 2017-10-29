#! /usr/bin/env python3

import unittest
import day15

class TestDay15(unittest.TestCase):
    def setUp(self):
        data = [
            'Disc #1 has 5 positions; at time=0, it is at position 4.',
            'Disc #2 has 2 positions; at time=0, it is at position 1.'
        ]
        self._disc_game = day15.DiscGame(data)

    def test_disc_positions(self):
        self.assertEqual(0, self._disc_game._disc_position(0, 1))
        self.assertEqual(1, self._disc_game._disc_position(1, 2))

    def test_push_button(self):
        self.assertEqual(False, self._disc_game._push_button(0))
        self.assertEqual(True, self._disc_game._push_button(5))

    def test_part1(self):
        self.assertEqual(5, self._disc_game.get_first_capsule())

if __name__ == '__main__':
    unittest.main()
