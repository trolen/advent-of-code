#! /usr/env python3

import unittest
import day10

class TestDay10(unittest.TestCase):
    def test_part1(self):
        raw_data = ['.#..#',
                    '.....',
                    '#####',
                    '....#',
                    '...##']
        grid = day10.Grid(raw_data)
        result = grid.find_best_station()
        self.assertEqual(8, result[2])
        raw_data = ['......#.#.',
                    '#..#.#....',
                    '..#######.',
                    '.#.#.###..',
                    '.#..#.....',
                    '..#....#.#',
                    '#..#....#.',
                    '.##.#..###',
                    '##...#..#.',
                    '.#....####']
        grid = day10.Grid(raw_data)
        result = grid.find_best_station()
        self.assertEqual(33, result[2])

    def test_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()