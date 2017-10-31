#! /usr/bin/env python3

import unittest
import day19

class TestDay19(unittest.TestCase):
    def test_part1(self):
        elf_circle = day19.ElfCircle(5)
        self.assertEqual(3, elf_circle.play_game())

    def test_part2(self):
        elf_circle = day19.ElfCircle(5)
        self.assertEqual(2, elf_circle.play_game(True))


if __name__ == '__main__':
    unittest.main()
