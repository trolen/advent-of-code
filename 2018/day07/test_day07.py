#! /usr/env python3

import day07
import unittest


class TestDay07(unittest.TestCase):
    def setUp(self):
        self._data = [
            'Step C must be finished before step A can begin.',
            'Step C must be finished before step F can begin.',
            'Step A must be finished before step B can begin.',
            'Step A must be finished before step D can begin.',
            'Step B must be finished before step E can begin.',
            'Step D must be finished before step E can begin.',
            'Step F must be finished before step E can begin.'
        ]

    def test_part1(self):
        (s, t) = day07.determine_order(self._data)
        self.assertEqual('CABDFE', s)

    def test_part2(self):
        (s, t) = day07.determine_order(self._data, num_workers=2, offset=0)
        self.assertEqual('CABFDE', s)
        self.assertEqual(15, t)


if __name__ == '__main__':
    unittest.main()