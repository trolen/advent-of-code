#!/usr/bin/env python3

import day7
import unittest

class TestDay7(unittest.TestCase):
  def test_evaluate_circuit(self):
    lines = ['123 -> x',
             '456 -> y',
             'x AND y -> d',
             'x OR y -> e',
             'x LSHIFT 2 -> f',
             'y RSHIFT 2 -> g',
             'NOT x -> h',
             'NOT y -> i']
    day7.load_circuit(lines)
    self.assertEqual(day7.evaluate('d'), 72)
    self.assertEqual(day7.evaluate('e'), 507)
    self.assertEqual(day7.evaluate('f'), 492)
    self.assertEqual(day7.evaluate('g'), 114)
    self.assertEqual(day7.evaluate('h'), 65412)
    self.assertEqual(day7.evaluate('i'), 65079)
    self.assertEqual(day7.evaluate('x'), 123)
    self.assertEqual(day7.evaluate('y'), 456)

if __name__ == '__main__':
  unittest.main()
