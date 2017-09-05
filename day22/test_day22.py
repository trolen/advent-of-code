#!/usr/bin/env python3

import day22
import unittest

class TestDay22(unittest.TestCase):
    def test_play_game(self):
        wizard = day22.Wizard(10, 0, 250)
        boss = day22.Boss(13, 0, 8)
        self.assertTrue(day22.play_game(wizard, boss))

if __name__ == "__main__":
    unittest.main()