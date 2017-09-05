#!/usr/bin/env python3

import day12
import unittest

class TestDay12(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(day12.sum_of_ints('[1,2,3]', False), 6)
    self.assertEqual(day12.sum_of_ints('{"a":2,"b":4}', False), 6)
    self.assertEqual(day12.sum_of_ints('[[[3]]]', False), 3)
    self.assertEqual(day12.sum_of_ints('{"a":{"b":4},"c":-1}', False), 3)
    self.assertEqual(day12.sum_of_ints('{"a":[1,-1]}', False), 0)
    self.assertEqual(day12.sum_of_ints('[-1,{"a":1}]', False), 0)
    self.assertEqual(day12.sum_of_ints('[]', False), 0)
    self.assertEqual(day12.sum_of_ints('{}', False), 0)

  def test_ignore_red(self):
    self.assertEqual(day12.sum_of_ints('[1,2,3]', True), 6)
    self.assertEqual(day12.sum_of_ints('[1,{"c":"red","b":2},3]', True), 4)
    self.assertEqual(day12.sum_of_ints('{"d":"red","e":[1,2,3,4],"f":5}', True), 0)
    self.assertEqual(day12.sum_of_ints('[1,"red",5]', True), 6)

if __name__ == '__main__':
  unittest.main()
