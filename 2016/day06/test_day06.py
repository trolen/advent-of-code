#! /usr/bin/env python3

import unittest
import day06

class TestDay06(unittest.TestCase):
    def setUp(self):
        self._data = [
            'eedadn',
            'drvtee',
            'eandsr',
            'raavrd',
            'atevrs',
            'tsrnev',
            'sdttsa',
            'rasrtv',
            'nssdts',
            'ntnada',
            'svetve',
            'tesnvt',
            'vntsnd',
            'vrdear',
            'dvrsen',
            'enarar'
        ]

    def test_part1(self):
        self.assertEqual(day06.decode_message1(self._data, 6), 'easter')

    def test_part2(self):
        self.assertEqual(day06.decode_message2(self._data, 6), 'advent')

if __name__ == '__main__':
    unittest.main()