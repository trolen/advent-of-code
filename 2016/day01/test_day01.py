#! /usr/bin/env python3

import unittest
import day01


class TestDay01(unittest.TestCase):
    _position = None

    def setUp(self):
        self._position = day01.Position()

    def test_example1(self):
        self._position.apply_instructions('R2, L3')
        self.assertEqual(self._position.get_distance(), 5)

    def test_example2(self):
        self._position.apply_instructions('R2, R2, R2')
        self.assertEqual(self._position.get_distance(), 2)

    def test_example3(self):
        self._position.apply_instructions('R5, L5, R5, R3')
        self.assertEqual(self._position.get_distance(), 12)

    def test_example4(self):
        self._position.apply_instructions('R8, R4, R4, R8', unique=True)
        self.assertEqual(self._position.get_distance(), 4)


if __name__ == '__main__':
    unittest.main()