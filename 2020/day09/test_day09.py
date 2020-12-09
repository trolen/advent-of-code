#! /usr/bin/env python3

import unittest
import day09


class TestDay09(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '35',
            '20',
            '15',
            '25',
            '47',
            '40',
            '62',
            '55',
            '65',
            '95',
            '102',
            '117',
            '150',
            '182',
            '127',
            '219',
            '299',
            '277',
            '309',
            '576'
        ]
        self.number_list = day09.parse_data(self.raw_data)
        self.key = day09.do_part1(self.number_list, 5)

    def test_part1(self):
        self.assertEqual(127, self.key)

    def test_part2(self):
        self.assertEqual(62, day09.do_part2(self.number_list, self.key))


if __name__ == '__main__':
    unittest.main()
