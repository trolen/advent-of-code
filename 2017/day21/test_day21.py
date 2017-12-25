#! /usr/bin/env python3

import unittest
import day21

class TestDay21(unittest.TestCase):
    def test_part1(self):
        data = [
            '../.# => ##./#../...',
            '.#./..#/### => #..#/..../..../#..#'
        ]
        prog = day21.Program(data)
        self.assertEqual(12, prog.run(2))


if __name__ == '__main__':
    unittest.main()