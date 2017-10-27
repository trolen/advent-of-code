#! /usr/bin/env python3

import unittest
import day11


class TestDay11(unittest.TestCase):
    def setUp(self):
        data = [
            'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
            'The second floor contains a hydrogen generator.',
            'The third floor contains a lithium generator.',
            'The fourth floor contains nothing relevant.'
        ]
        self._sim = day11.Simulator(data)

    def test_1(self):
        self.assertEqual(self._sim.play_game(), 11)


if __name__ == '__main__':
    unittest.main()
