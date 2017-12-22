#! /usr/bin/env python3

import unittest
import day20

class TestDay20(unittest.TestCase):
    def test_part1(self):
        data = [
            'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
            'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'
        ]
        particles = day20.Particles(data)
        self.assertEqual(0, particles.find_min_accel())

    def test_part2(self):
        data = [
            'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
            'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
            'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
            'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>'
        ]
        particles = day20.Particles(data)
        self.assertEqual(1, particles.run())


if __name__ == '__main__':
    unittest.main()
