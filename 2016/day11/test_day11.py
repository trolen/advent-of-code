#! /usr/bin/env python3

import unittest
import day11

class TestDay11(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
            'The second floor contains a hydrogen generator.',
            'The third floor contains a lithium generator.',
            'The fourth floor contains nothing relevant.'
        ]

    def test_part1(self):
        app = day11.Application(self.raw_data)
        pass


if __name__ == '__main__':
    unittest.main()
