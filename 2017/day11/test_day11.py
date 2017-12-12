#! /usr/bin/env python3

import unittest
import day11

class TestDay11(unittest.TestCase):
    def test_part1(self):
        hex_grid = day11.HexGrid()
        hex_grid.follow_directions('ne,ne,ne')
        self.assertEqual(3, hex_grid.steps_from_start())
        hex_grid.reset().follow_directions('ne,ne,sw,sw')
        self.assertEqual(0, hex_grid.steps_from_start())
        hex_grid.reset().follow_directions('ne,ne,s,s')
        self.assertEqual(2, hex_grid.steps_from_start())
        hex_grid.reset().follow_directions('se,sw,se,sw,sw')
        self.assertEqual(3, hex_grid.steps_from_start())


if __name__ == '__main__':
    unittest.main()
