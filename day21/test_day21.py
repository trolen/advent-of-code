#!/usr/bin/env python3

import day21
import unittest

class TestDay21(unittest.TestCase):
  def test_1(self):
    boss = day21.Player(12, 7, 2)
    player = day21.Player(8, 5, 5)
    winner = day21.play_game(boss, player)
    self.assertEqual(winner, 'Player')

if __name__ == '__main__':
  unittest.main()
