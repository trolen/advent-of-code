#! /usr/bin/env python3

import unittest
import day22

class TestDay22(unittest.TestCase):
    def setUp(self):
        data = [
            '..#',
            '#..',
            '...'
        ]
        self._cluster = day22.Cluster(data)

    def test_part1(self):
        self.assertEqual(5, self._cluster.run(7))
        self.assertEqual(41, self._cluster.run(70))
        self.assertEqual(5587, self._cluster.run(10000))

    def test_part2(self):
        self.assertEqual(26, self._cluster.run(100, part2=True))
        self.assertEqual(2511944, self._cluster.run(10000000, part2=True))


if __name__ == '__main__':
    unittest.main()
