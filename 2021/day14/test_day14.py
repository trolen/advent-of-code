#! /usr/bin/env python3

import unittest
import day14


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'NNCB',
            '',
            'CH -> B',
            'HH -> N',
            'CB -> H',
            'NH -> C',
            'HB -> C',
            'HC -> B',
            'HN -> C',
            'NN -> C',
            'BH -> H',
            'NC -> B',
            'NB -> B',
            'BN -> B',
            'BB -> N',
            'BC -> B',
            'CC -> N',
            'CN -> C'
        ]

    def test_part1(self):
        self.assertEqual(1588, day14.do_part1(self.raw_data))

    def test_part2(self):
        self.assertEqual(2188189693529, day14.do_part2(self.raw_data))


if __name__ == '__main__':
    unittest.main()
