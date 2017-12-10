#! /usr/bin/env python3

import unittest
import day10

class TestDay10(unittest.TestCase):
    def test_part1(self):
        knot_hash = day10.KnotHash(5)
        self.assertEqual(12, knot_hash.hash_one('3,4,1,5'))

    def test_part2(self):
        knot_hash = day10.KnotHash(256)
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', knot_hash.hash_64(''))
        knot_hash.reset()
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', knot_hash.hash_64('AoC 2017'))
        knot_hash.reset()
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', knot_hash.hash_64('1,2,3'))
        knot_hash.reset()
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', knot_hash.hash_64('1,2,4'))


if __name__ == '__main__':
    unittest.main()