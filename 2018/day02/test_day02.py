#! /usr/env python3

import day02
import unittest


class TestDay02(unittest.TestCase):
    def test_part1(self):
        data = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab'
        ]
        checksum = day02.calc_checksum(data)
        self.assertEqual(12, checksum)

    def test_part2(self):
        data = [
            'abcde',
            'fghij',
            'klmno',
            'pqrst',
            'fguij',
            'axcye',
            'wvxyz'
        ]
        s = day02.find_matching_string(data)
        self.assertEqual('fgij', s)


if __name__ == '__main__':
    unittest.main()