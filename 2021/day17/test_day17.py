#! /usr/bin/env python3

import unittest
import day17


class TestDay17(unittest.TestCase):
    def setUp(self):
        self._raw_data = ['target area: x=20..30, y=-10..-5']

    def test_parse_data(self):
        probe = day17.Probe(self._raw_data)
        xrange, yrange = probe.target_area()
        self.assertEqual((20, 30), xrange)
        self.assertEqual((-10, -5), yrange)

    def test_fire_probe(self):
        probe = day17.Probe(self._raw_data)
        self.assertTrue(probe.fire_probe(7, 2))
        self.assertTrue(probe.fire_probe(6, 3))
        self.assertFalse(probe.fire_probe(17, -4))
        self.assertTrue(probe.fire_probe(6, 9))

    def test_part1(self):
        self.assertEqual(45, day17.do_part1(self._raw_data))

    def test_part2(self):
        self.assertEqual(112, day17.do_part2(self._raw_data))


if __name__ == '__main__':
    unittest.main()
