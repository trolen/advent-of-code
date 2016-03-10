#!/usr/bin/env python3

import fileinput
import sys

OPERATIONS=['AND', 'OR', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT']

circuit = []

def load_circuit(lines):
  global circuit
  del circuit[:]
  for line in lines:
    line = line.rstrip().split(' -> ')
    target = line[1]
    expr = line[0].split(' ')
    oper = ''
    arg1 = ''
    arg2 = ''
    for term in expr:
      if term in OPERATIONS:
        oper = term
      elif arg1 == '':
        arg1 = term
      else:
        arg2 = term
    circuit.append([target, oper, arg1, arg2, None])

def evaluate(s):
  global circuit
  try:
    value = int(s)
    return value
  except:
    pass
  for expr in circuit:
    if s == expr[0]:
      oper = expr[1]
      arg1 = expr[2]
      arg2 = expr[3]
      value = expr[4]
      if value != None:
        return value
      if oper == '':
        value = evaluate(arg1)
      elif oper == 'AND':
        value = evaluate(arg1) & evaluate(arg2)
      elif oper == 'OR':
        value = evaluate(arg1) | evaluate(arg2)
      elif oper == 'NOT':
        value = ~evaluate(arg1)
      elif oper == 'XOR':
        value = evaluate(arg1) ^ evaluate(arg2)
      elif oper == 'LSHIFT':
        value = evaluate(arg1) << evaluate(arg2)
      elif oper == 'RSHIFT':
        value = evaluate(arg1) >> evaluate(arg2)
      if value != None:
        expr[4] = value
        return 0xffff & value
  print("ERROR: String (%s) not found in evaluate()" % s)
  sys.exit(-1)
  return 0

def assign(target, value):
  global circuit
  for expr in circuit:
    if target == expr[0]:
      expr[4] = value

if __name__ == '__main__':
  lines = [line for line in fileinput.input()]
  print("Loading circuit...")
  load_circuit(lines)
  value = evaluate('a')
  print("Evaluate a -> %s" % value)
  print("Reloading circuit...")
  load_circuit(lines)
  print("Assign b <- %s" % value)
  assign('b', value)
  print("Evaluate a -> %s" % evaluate('a'))
