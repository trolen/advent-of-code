#! /usr/bin/env python3

import unittest
import day14

class TestDay14(unittest.TestCase):
    def test_hash1(self):
        commpad = day14.CommPad('abc')
        self.assertEqual(commpad._calculate_hash('abc0'), '577571be4de9dcce85a041ba0410f29f')

    def test_hash2(self):
        commpad = day14.CommPad('abc', True)
        self.assertEqual(commpad._calculate_hash('abc0'), 'a107ff634856bb300138cac6568c0f24')

    def test_part1(self):
        commpad = day14.CommPad('abc')
        self.assertEqual(commpad.find_keys(64), 22728)

    def test_part2(self):
        commpad = day14.CommPad('abc', True)
        self.assertEqual(commpad.find_keys(64), 22551)


if __name__ == '__main__':
    unittest.main()
