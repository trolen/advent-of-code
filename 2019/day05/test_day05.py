#! /usr/env python3

import unittest
import day05


class TestDay05(unittest.TestCase):
    def test_part1(self):
        data = day05.run_intcode('1002,4,3,4,33')
        self.assertEqual([1002, 4, 3, 4, 99], data)
        data = day05.run_intcode('1101,100,-1,4,0')
        self.assertEqual([1101, 100, -1, 4, 99], data)

    def test_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()