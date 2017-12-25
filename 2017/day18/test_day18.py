#! /usr/bin/env python3

import unittest
import day18

class TestDay18(unittest.TestCase):
    def test_part1(self):
        instructions = [
            'set a 1',
            'add a 2',
            'mul a a',
            'mod a 5',
            'snd a',
            'set a 0',
            'rcv a',
            'jgz a -1',
            'set a 1',
            'jgz a -2'
        ]
        self.assertEqual(4, day18.solo(instructions))

    def test_part2(self):
        instructions = [
            'snd 1',
            'snd 2',
            'snd p',
            'rcv a',
            'rcv b',
            'rcv c',
            'rcv d'
        ]
        self.assertEqual(3, day18.duet(instructions))


if __name__ == '__main__':
    unittest.main()
