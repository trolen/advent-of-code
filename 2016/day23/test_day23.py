#! /usr/bin/env python3

import unittest
import day23

class TestDay23(unittest.TestCase):
    def test_part1(self):
        data = [
            'cpy 2 a',
            'tgl a',
            'tgl a',
            'tgl a',
            'cpy 1 a',
            'dec a',
            'dec a'
        ]
        interpreter = day23.Interpreter()
        interpreter.interpret_instructions(data)
        self.assertEqual(3, interpreter.get_register('a'))

if __name__ == '__main__':
    unittest.main()
