#! /usr/env python3

import unittest
import day06


class TestDay06(unittest.TestCase):
    def setUp(self):
        raw_data = ['COM)B',
                    'B)C',
                    'C)D',
                    'D)E',
                    'E)F',
                    'B)G',
                    'G)H',
                    'D)I',
                    'E)J',
                    'J)K',
                    'K)L',
                    'K)YOU',
                    'I)SAN']
        self._orbits = day06.parse_orbits(raw_data)

    def test_part1(self):
        cnt = day06.count_orbits(self._orbits)
        self.assertEqual(54, cnt)

    def test_part2(self):
        cnt = day06.find_santa(self._orbits, 'YOU')
        self.assertEqual(4, cnt)


if __name__ == '__main__':
    unittest.main()