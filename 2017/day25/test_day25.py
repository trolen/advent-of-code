#! /usr/bin/env python3

import unittest
import day25

class TestDay25(unittest.TestCase):
    def setUp(self):
        data = day25.read_data('test_input.txt')
        self._tape = day25.Tape(data)

    def test_part1(self):
        self.assertEqual(3, self._tape.run())


if __name__ == '__main__':
    unittest.main()
