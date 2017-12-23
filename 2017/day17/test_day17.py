#! /usr/bin/env python3

import unittest
import day17

class TestDay17(unittest.TestCase):
    def setUp(self):
        self._spinlock = day17.Spinlock(3)

    def test_part1(self):
        self.assertEqual(638, self._spinlock.run(2017))

    def test_part2(self):
        self.assertEqual(1226, self._spinlock.run(2017, part2=True))

if __name__ == '__main__':
    unittest.main()
