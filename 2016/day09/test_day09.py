#! /usr/bin/env python3

import unittest
import day09


class TestDay09(unittest.TestCase):
    def test_nodecrypt(self):
        self.assertEqual(day09.get_length1('ADVENT'), 6)

    def test_decrypt(self):
        self.assertEqual(day09.get_length1('A(1x5)BC'), 7)
        self.assertEqual(day09.get_length1('(3x3)XYZ'), 9)

    def test_decrypt2(self):
        self.assertEqual(day09.get_length2('(3x3)XYZ'), 9)
        self.assertEqual(day09.get_length2('X(8x2)(3x3)ABCY'), 20)


if __name__ == '__main__':
    unittest.main()