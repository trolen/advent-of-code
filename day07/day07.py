#!/usr/bin/env python3

import fileinput
import sys

class Wire:
  def __init__(self, name, oper, arg1, arg2):
    self.name = name
    self.oper = oper
    self.arg1 = arg1
    self.arg2 = arg2
    self._value = None

  def reset(self):
    self._value = None

  def get(self):
    return self._value

  def set(self, value):
    self._value = 0xffff & value

class Circuit:
  def __init__(self, lines):
    self._wires = []
    self._parse_lines(lines)
    
  def _parse_lines(self, lines):
    for line in lines:
      expr = line.rstrip().split(' ')
      wire = expr[-1]
      oper = None
      arg1 = None
      arg2 = None
      n = len(expr)
      if n == 3:
        arg1 = expr[0]
      elif n == 4:
        oper = expr[0]
        arg1 = expr[1]
      elif n == 5:
        arg1 = expr[0]
        oper = expr[1]
        arg2 = expr[2]
      self._wires.append(Wire(wire, oper, arg1, arg2))

  def reset(self):
    for wire in self._wires:
      wire.reset()

  def set(self, name, value):
    for wire in self._wires:
      if name == wire.name:
        wire.set(value)

  def get(self, name):
    for wire in self._wires:
      if name == wire.name:
        return wire.get()

  def run(self):
    for wire in self._wires:
      self._evaluate(wire.name)

  def _evaluate(self, s):
    try:
      value = int(s)
      return value
    except:
      pass
    for wire in self._wires:
      if s == wire.name:
        if wire.get() is not None:
          return wire.get()
        if wire.oper is None:
          wire.set(self._evaluate(wire.arg1))
        elif wire.oper == 'AND':
          wire.set(self._evaluate(wire.arg1) & self._evaluate(wire.arg2))
        elif wire.oper == 'OR':
          wire.set(self._evaluate(wire.arg1) | self._evaluate(wire.arg2))
        elif wire.oper == 'NOT':
          wire.set(~self._evaluate(wire.arg1))
        elif wire.oper == 'XOR':
          wire.set(self._evaluate(wire.arg1) ^ self._evaluate(wire.arg2))
        elif wire.oper == 'LSHIFT':
          wire.set(self._evaluate(wire.arg1) << self._evaluate(wire.arg2))
        elif wire.oper == 'RSHIFT':
          wire.set(self._evaluate(wire.arg1) >> self._evaluate(wire.arg2))
        if wire.get() is not None:
          return wire.get()
    return None

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == '__main__':
  lines = read_input()
  circuit = Circuit(lines)
  print("Running circuit...")
  circuit.run()
  value = circuit.get('a')
  print("a -> %s" % value)
  print("Resetting circuit...")
  circuit.reset()
  print("Assign b <- %s" % value)
  circuit.set('b', value)
  print("Running circuit...")
  circuit.run()
  print("a -> %s" % circuit.get('a'))
