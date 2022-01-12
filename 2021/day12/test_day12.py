#! /usr/bin/env python3

import unittest
import day12


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.raw_data1 = [
            'start-A',
            'start-b',
            'A-c',
            'A-b',
            'b-d',
            'A-end',
            'b-end'
        ]
        self.raw_data2 = [
            'dc-end',
            'HN-start',
            'start-kj',
            'dc-start',
            'dc-HN',
            'LN-dc',
            'HN-end',
            'kj-sa',
            'kj-HN',
            'kj-dc'
        ]
        self.raw_data3 = [
            'fs-end',
            'he-DX',
            'fs-he',
            'start-DX',
            'pj-DX',
            'end-zg',
            'zg-sl',
            'zg-pj',
            'pj-he',
            'RW-he',
            'fs-DX',
            'pj-RW',
            'zg-RW',
            'start-pj',
            'he-WI',
            'zg-he',
            'pj-fs',
            'start-RW'
        ]

    def test_part1(self):
        self.assertEqual(10, day12.do_part1(self.raw_data1))
        self.assertEqual(19, day12.do_part1(self.raw_data2))
        self.assertEqual(226, day12.do_part1(self.raw_data3))

    def test_part2(self):
        self.assertEqual(36, day12.do_part2(self.raw_data1))
        self.assertEqual(103, day12.do_part2(self.raw_data2))
        self.assertEqual(3509, day12.do_part2(self.raw_data3))


if __name__ == '__main__':
    unittest.main()
