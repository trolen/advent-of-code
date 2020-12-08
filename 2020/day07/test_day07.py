#! /usr/bin/env python3

import unittest
import day07


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.',
            'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
            'bright white bags contain 1 shiny gold bag.',
            'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
            'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
            'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
            'faded blue bags contain no other bags.',
            'dotted black bags contain no other bags.'
        ]
        self.rules = day07.parse_data(self.raw_data)

    def test_part1(self):
        self.assertEqual(4, day07.do_part1(self.rules))

    def test_part2(self):
        self.assertEqual(32, day07.do_part2(self.rules))


if __name__ == '__main__':
    unittest.main()
