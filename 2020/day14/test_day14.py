#! /usr/bin/env python3

import unittest
import day14


class TestDay13(unittest.TestCase):
    def setUp(self):
        pass

    def test_part1(self):
        raw_data = [
            'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'mem[8] = 11',
            'mem[7] = 101',
            'mem[8] = 0'
        ]
        app1 = day14.Application(raw_data)
        self.assertEqual(165, app1.do_part1())

    def test_part2(self):
        raw_data = [
            'mask = 000000000000000000000000000000X1001X',
            'mem[42] = 100',
            'mask = 00000000000000000000000000000000X0XX',
            'mem[26] = 1'
        ]
        app2 = day14.Application(raw_data)
        self.assertEqual(208, app2.do_part2())


if __name__ == '__main__':
    unittest.main()
