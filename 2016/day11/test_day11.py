#! /usr/bin/env python3

import unittest
import day11


class TestDay11(unittest.TestCase):
    def setUp(self):
        self._input = [
            'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
            'The second floor contains a hydrogen generator.',
            'The third floor contains a lithium generator.',
            'The fourth floor contains nothing relevant.'
        ]


if __name__ == '__main__':
    unittest.main()
