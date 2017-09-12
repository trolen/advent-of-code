#! /usr/bin/env python3

import unittest
import day07


class TestDay7(unittest.TestCase):
    def test_is_abba(self):
        self.assertTrue(day07.is_abba('abba'))
        self.assertFalse(day07.is_abba('mnop'))

    def test_contains_abba(self):
        self.assertTrue(day07.contains_abba('ioxxoj'))
        self.assertFalse(day07.contains_abba('asdfgh'))

    def test_supports_tls(self):
        self.assertTrue(day07.supports_tls('abba[mnop]qrst'))
        self.assertFalse(day07.supports_tls('abcd[bddb]xyyx'))


if __name__ == '__main__':
    unittest.main()