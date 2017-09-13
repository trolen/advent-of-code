#! /usr/bin/env python3

import unittest
import day08


class TestDay08(unittest.TestCase):
    def setUp(self):
        self.screen = day08.Screen(7, 3)

    def test_rect(self):
        self.screen.rect(3, 2)
        self.assertEqual(self.screen.count_on(), 6)
        self.assertEqual(self.screen.show(), ['###....', '###....', '.......'])

    def test_rotate_column(self):
        self.screen.rect(3, 2)
        self.screen.rotate_column(1, 1)
        self.assertEqual(self.screen.count_on(), 6)
        self.assertEqual(self.screen.show(), ['#.#....', '###....', '.#.....'])

    def test_rotate_row(self):
        self.screen.rect(3, 2)
        self.screen.rotate_column(1, 1)
        self.screen.rotate_row(0, 4)
        self.assertEqual(self.screen.count_on(), 6)
        self.assertEqual(self.screen.show(), ['....#.#', '###....', '.#.....'])


if __name__ == '__main__':
    unittest.main()
