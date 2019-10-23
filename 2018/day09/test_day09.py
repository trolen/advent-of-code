#! /usr/env python3

import day09
import unittest


class TestDay08(unittest.TestCase):
    def test_part1(self):
        score = day09.play_game('9 players; last marble is worth 25 points')
        self.assertEqual(32, score)
        score = day09.play_game('10 players; last marble is worth 1618 points')
        self.assertEqual(8317, score)


if __name__ == '__main__':
    unittest.main()
