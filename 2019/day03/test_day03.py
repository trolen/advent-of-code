#! /usr/env python3

import unittest
import day03


class TestDay03(unittest.TestCase):
    def test_part1(self):
        raw_data = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
        crossings = day03.find_crossings(raw_data)
        distance = day03.find_closest_crossing(crossings)
        self.assertEqual(6, distance)
        raw_data = ['R75,D30,R83,U83,L12,D49,R71,U7,L7', 'U62,R66,U55,R34,D71,R55,D58,R83']
        crossings = day03.find_crossings(raw_data)
        distance = day03.find_closest_crossing(crossings)
        self.assertEqual(159, distance)
        raw_data = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
        crossings = day03.find_crossings(raw_data)
        distance = day03.find_closest_crossing(crossings)
        self.assertEqual(135, distance)

    def test_part2(self):
        raw_data = ['R8,U5,L5,D3', 'U7,R6,D4,L4']
        crossings = day03.find_crossings(raw_data)
        steps = day03.find_fewest_steps(crossings)
        self.assertEqual(30, steps)
        raw_data = ['R75,D30,R83,U83,L12,D49,R71,U7,L7', 'U62,R66,U55,R34,D71,R55,D58,R83']
        crossings = day03.find_crossings(raw_data)
        steps = day03.find_fewest_steps(crossings)
        self.assertEqual(610, steps)
        raw_data = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']
        crossings = day03.find_crossings(raw_data)
        steps = day03.find_fewest_steps(crossings)
        self.assertEqual(410, steps)


if __name__ == '__main__':
    unittest.main()