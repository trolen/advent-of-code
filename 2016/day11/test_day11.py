#! /usr/bin/env python3


import unittest
import day11

class TestDay11(unittest.TestCase):
    def setUp(self):
        self._data = [
            'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
            'The second floor contains a hydrogen generator.',
            'The third floor contains a lithium generator.',
            'The fourth floor contains nothing relevant.'
        ]

    def test_part1(self):
        result, _ = day11.do_part1(self._data)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()
