#!/usr/bin/env python3

import day15
import unittest


class TestDay15(unittest.TestCase):
    def setUp(self):
        raw_data = [
            '#######',
            '#.G...#',
            '#...EG#',
            '#.#.#G#',
            '#..G#E#',
            '#.....#',
            '#######'
        ]
        self.app = day15.Application(raw_data)

    def test_part1(self):
        self.assertEqual(27730, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(4988, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
