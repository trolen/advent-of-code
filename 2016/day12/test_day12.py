#! /usr/bin/env python3

import unittest
import day12

class TestDay12(unittest.TestCase):
    def test_part1(self):
        data = ['cpy 41 a',
                'inc a',
                'inc a',
                'dec a',
                'jnz a 2',
                'dec a']
        computer = day12.Computer()
        computer.process_instructions(data)
        self.assertEqual(computer.get_register('a'), 42)


if __name__ == '__main__':
    unittest.main()