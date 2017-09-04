#!/usr/bin/env python3

import day22
import unittest

class TestDay22(unittest.TestCase):
    def test_play_game(self):
        player = day22.Wizard(10, 250)
        boss = day22.Boss(13, 8)

if __name__ == "__main__":
    unittest.main()