#! /usr/env python3

import unittest
import day02


class TestDay02(unittest.TestCase):
    def test_part1(self):
        data = day02.run_intcode('1,0,0,0,99')
        self.assertEqual([2,0,0,0,99], data)
        data = day02.run_intcode('2,3,0,3,99')
        self.assertEqual([2,3,0,6,99], data)
        data = day02.run_intcode('2,4,4,5,99,0')
        self.assertEqual([2,4,4,5,99,9801], data)
        data = day02.run_intcode('1,1,1,4,99,5,6,0,99')
        self.assertEqual([30,1,1,4,2,5,6,0,99], data)

    def test_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()