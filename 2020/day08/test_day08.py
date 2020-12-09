#! /usr/bin/env python3

import unittest
import day08


class TestDay07(unittest.TestCase):
    def setUp(self):
        pass

    def test_part1(self):
        raw_data = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6'
        ]
        instructions = day08.parse_data(raw_data)
        self.assertEqual(5, day08.run_program(instructions))

    def test_part2(self):
        raw_data = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'nop -4',
            'acc +6'
        ]
        instructions = day08.parse_data(raw_data)
        self.assertEqual(8, day08.run_program(instructions))


if __name__ == '__main__':
    unittest.main()
