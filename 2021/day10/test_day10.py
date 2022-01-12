#! /usr/bin/env python3

import unittest
import day10


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
          '[({(<(())[]>[[{[]{<()<>>',
          '[(()[<>])]({[<{<<[]>>(',
          '{([(<{}[<>[]}>{[]{[(<()>',
          '(((({<>}<{<{<>}{[]{[]{}',
          '[[<[([]))<([[{}[[()]]]',
          '[{[{({}]{}}([{[{{{}}([]',
          '{<[[]]>}<{[{[{[]{()[[[]',
          '[<(<(<(<{}))><([]([]()',
          '<{([([[(<>()){}]>(<<{{',
          '<{([{{}}[<[[[<>{}]]]>[]]'
        ]

    def test_part1(self):
        self.assertEqual(26397, day10.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(288957, day10.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
