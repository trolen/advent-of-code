#!/usr/bin/env python3

import day22
import unittest


class TestDay22(unittest.TestCase):
    def test_pt1_1(self):
        sim = day22.Simulator(day22.Player(10, 250), day22.Boss(13, 8))
        self.assertEqual(sim.run(), 226)

    def test_pt1_2(self):
        sim = day22.Simulator(day22.Player(10, 250), day22.Boss(14, 8))
        self.assertEqual(sim.run(), 641)


if __name__ == "__main__":
    unittest.main()