#! /usr/bin/env python3

import unittest
import day14

class TestDay14(unittest.TestCase):
    def setUp(self):
        self._defrag = day14.Defragmenter('flqrgnkx')

    def test_count_bits(self):
        self.assertEqual(8108, self._defrag.count_bits())

    def test_count_regions(self):
        self.assertEqual(1242, self._defrag.count_regions())


if __name__ == '__main__':
    unittest.main()
