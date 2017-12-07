#! /usr/bin/env python3

import unittest
import day06

class TestDay6(unittest.TestCase):
    def setUp(self):
        data = '0 2 7 0'
        self.debugger = day06.Debugger(data)

    def test_reallocation(self):
        self.assertEqual(5, self.debugger.reallocate_blocks())

    def test_loop_size(self):
        self.debugger.reallocate_blocks()
        self.assertEqual(4, self.debugger.get_loop_size())


if __name__ == '__main__':
    unittest.main()
