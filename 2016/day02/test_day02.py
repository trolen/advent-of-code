#! /usr/bin/env python3

import unittest
import day02

class TestDay02(unittest.TestCase):
    def setUp(self):
        self.input_strings = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]

    def test_keypad1(self):
        self.assertEqual(day02.get_code(day02.KEYPAD1, self.input_strings), '1985')

    def test_keypad2(self):
        self.assertEqual(day02.get_code(day02.KEYPAD2, self.input_strings), '5DB3')


if __name__ == '__main__':
    unittest.main()