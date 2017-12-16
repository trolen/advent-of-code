#! /usr/bin/env python3

import unittest
import day15

class TestDay15(unittest.TestCase):
    def setUp(self):
        self._gen_a = day15.GeneratorA(65)
        self._gen_b = day15.GeneratorB(8921)

    def test_gena(self):
        self.assertEqual(1092455, self._gen_a.next())
        self.assertEqual(1181022009, self._gen_a.next())
        self.assertEqual(245556042, self._gen_a.next())
        self.assertEqual(1744312007, self._gen_a.next())
        self.assertEqual(1352636452, self._gen_a.next())

    def test_genb(self):
        self.assertEqual(430625591, self._gen_b.next())
        self.assertEqual(1233683848, self._gen_b.next())
        self.assertEqual(1431495498, self._gen_b.next())
        self.assertEqual(137874439, self._gen_b.next())
        self.assertEqual(285222916, self._gen_b.next())

    def test_1_short(self):
        self.assertEqual(1, day15.compare_generators(self._gen_a, self._gen_b, 5))

    def test_1_full(self):
        self.assertEqual(588, day15.compare_generators(self._gen_a, self._gen_b, 40000000))

    def test_gena_mult(self):
        self.assertEqual(1352636452, self._gen_a.next(use_mult=True))
        self.assertEqual(1992081072, self._gen_a.next(use_mult=True))
        self.assertEqual(530830436, self._gen_a.next(use_mult=True))
        self.assertEqual(1980017072, self._gen_a.next(use_mult=True))
        self.assertEqual(740335192, self._gen_a.next(use_mult=True))

    def test_genb_mult(self):
        self.assertEqual(1233683848, self._gen_b.next(use_mult=True))
        self.assertEqual(862516352, self._gen_b.next(use_mult=True))
        self.assertEqual(1159784568, self._gen_b.next(use_mult=True))
        self.assertEqual(1616057672, self._gen_b.next(use_mult=True))
        self.assertEqual(412269392, self._gen_b.next(use_mult=True))

    def test_2_short(self):
        self.assertEqual(1, day15.compare_generators(self._gen_a, self._gen_b, 1060, use_mult=True))

    def test_2_full(self):
        self.assertEqual(309, day15.compare_generators(self._gen_a, self._gen_b, 5000000, use_mult=True))


if __name__ == '__main__':
    unittest.main()
