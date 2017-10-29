#! /usr/bin/env python3

import unittest
import day16

class TestDay16(unittest.TestCase):
    def setUp(self):
        self._disk = day16.Disk(20, '10000')

    def test_dragon_curve(self):
        self.assertEqual('100', self._disk._dragon_curve('1'))
        self.assertEqual('001', self._disk._dragon_curve('0'))
        self.assertEqual('11111000000', self._disk._dragon_curve('11111'))
        self.assertEqual('1111000010100101011110000', self._disk._dragon_curve('111100001010'))

    def test_checksum(self):
        self.assertEqual('100', self._disk._compute_checksum('110010110100'))

    def test_part1(self):
        self.assertEqual('01100', self._disk.fill_disk())


if __name__ == '__main__':
    unittest.main()
