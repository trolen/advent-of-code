#!/usr/bin/env python3

import day07
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
    circuit = day07.Circuit(lines)
    circuit.run()
    self.assertEqual(circuit.get('d'), 72)
    self.assertEqual(circuit.get('e'), 507)
    self.assertEqual(circuit.get('f'), 492)
    self.assertEqual(circuit.get('g'), 114)
    self.assertEqual(circuit.get('h'), 65412)
    self.assertEqual(circuit.get('i'), 65079)
    self.assertEqual(circuit.get('x'), 123)
    self.assertEqual(circuit.get('y'), 456)

if __name__ == '__main__':
  unittest.main()
