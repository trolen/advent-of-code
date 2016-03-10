#!/usr/bin/env python3

import fileinput

class Circuit:
  def __init__(self, lines):
    self._operations = ['AND', 'OR', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT']
    self._circuit = []
    for line in lines:
      line = line.rstrip().split(' -> ')
      wire = line[1]
      expr = line[0].split(' ')
      oper = ''
      arg1 = ''
      arg2 = ''
      for term in expr:
        if term in self._operations:
          oper = term
        elif arg1 == '':
          arg1 = term
        else:
          arg2 = term
      self._circuit.append([wire, oper, arg1, arg2, None])

  def reset(self):
    for expr in self._circuit:
      expr[4] = None

  def set(self, wire, value):
    for expr in self._circuit:
      if wire == expr[0]:
        expr[4] = value

  def get(self, wire):
    for expr in self._circuit:
      if wire == expr[0]:
        return expr[4]

  def run(self):
    for expr in self._circuit:
      self._evaluate(expr[0])

  def _evaluate(self, s):
    try:
      value = int(s)
      return value
    except:
      pass
    for expr in self._circuit:
      if s == expr[0]:
        oper = expr[1]
        arg1 = expr[2]
        arg2 = expr[3]
        value = expr[4]
        if value != None:
          return value
        if oper == '':
          value = self._evaluate(arg1)
        elif oper == 'AND':
          value = self._evaluate(arg1) & self._evaluate(arg2)
        elif oper == 'OR':
          value = self._evaluate(arg1) | self._evaluate(arg2)
        elif oper == 'NOT':
          value = ~self._evaluate(arg1)
        elif oper == 'XOR':
          value = self._evaluate(arg1) ^ self._evaluate(arg2)
        elif oper == 'LSHIFT':
          value = self._evaluate(arg1) << self._evaluate(arg2)
        elif oper == 'RSHIFT':
          value = self._evaluate(arg1) >> self._evaluate(arg2)
        if value != None:
          expr[4] = 0xffff & value
          return expr[4]
    return None

if __name__ == '__main__':
  circuit = Circuit([line for line in fileinput.input()])
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
  print("Evaluate a -> %s" % circuit.get('a'))
