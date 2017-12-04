#! /usr/bin/env python3

import unittest
import day04

class TestDay04(unittest.TestCase):
    def test_is_valid1(self):
        self.assertTrue(day04.is_valid1('aa bb cc dd ee'))
        self.assertFalse(day04.is_valid1('aa bb cc dd aa'))
        self.assertTrue(day04.is_valid1('aa bb cc dd aaa'))

    def test_is_valid2(self):
        self.assertTrue(day04.is_valid2('abcde fghij'))
        self.assertFalse(day04.is_valid2('abcde xyz ecdab'))
        self.assertTrue(day04.is_valid2('a ab abc abd abf abj'))
        self.assertTrue(day04.is_valid2('iiii oiii ooii oooi oooo'))
        self.assertFalse(day04.is_valid2('oiii ioii iioi iiio'))


if __name__ == '__main__':
    unittest.main()
