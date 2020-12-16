#! /usr/bin/env python3

import unittest
import day16


class TestDay16(unittest.TestCase):
    def test_part1(self):
        raw_data = [
            'class: 1-3 or 5-7',
            'row: 6-11 or 33-44',
            'seat: 13-40 or 45-50',
            '',
            'your ticket:',
            '7,1,14',
            '',
            'nearby tickets:',
            '7,3,47',
            '40,4,50',
            '55,2,20',
            '38,6,12'
        ]
        app = day16.Application(raw_data)
        self.assertEqual(71, app.do_part1())

    def test_part2(self):
        raw_data = [
            'class: 0-1 or 4-19',
            'row: 0-5 or 8-19',
            'seat: 0-13 or 16-19',
            '',
            'your ticket:',
            '11,12,13',
            '',
            'nearby tickets:',
            '3,9,18',
            '15,1,5',
            '5,14,9'
        ]
        app = day16.Application(raw_data)
        self.assertTrue(app._identify_fields())
        self.assertEqual(12, app.get_field_value('class'))
        self.assertEqual(11, app.get_field_value('row'))
        self.assertEqual(13, app.get_field_value('seat'))


if __name__ == '__main__':
    unittest.main()
