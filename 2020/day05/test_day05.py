#! /usr/bin/env python3

import unittest
import day05


class TestDay05(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'FBFBBFFRLR',
            'BFFFBBFRRR',
            'FFFBBBFRRR',
            'BBFFBBFRLL'
        ]
        self.seat_numbers = day05.parse_data(self.raw_data)

    def test_parse_line(self):
        self.assertEqual(357, day05.parse_line('FBFBBFFRLR'))
        self.assertEqual(567, day05.parse_line('BFFFBBFRRR'))

    def test_part1(self):
        self.assertEqual(820, day05.do_part1(self.seat_numbers))

    def test_part2(self):
        self.assertEqual(120, day05.do_part2(self.seat_numbers))


if __name__ == '__main__':
    unittest.main()
