#!/usr/bin/env python3

import day21
import unittest

class TestDay21(unittest.TestCase):
  def test_play_game(self):
    boss = day21.Player(12, 7, 2)
    player = day21.Player(8, 5, 5)
    self.assertTrue(day21.play_game(boss, player))

if __name__ == '__main__':
  unittest.main()
