#! /usr/bin/env python3

import unittest
import day02

class TestDay2(unittest.TestCase):
    def test_part1(self):
        data = [
            '5 1 9 5',
            '7 5 3',
            '2 4 6 8'
        ]
        spreadsheet = day02.Spreadsheet(data)
        self.assertEqual(18, spreadsheet.get_checksum1())

    def test_part2(self):
        data = [
            '5 9 2 8',
            '9 4 7 3',
            '3 8 6 5'
        ]
        spreadsheet = day02.Spreadsheet(data)
        self.assertEqual(9, spreadsheet.get_checksum2())


if __name__ == '__main__':
    unittest.main()
