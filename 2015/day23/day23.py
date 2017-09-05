#!/usr/bin/env python3

import fileinput
import sys
from pypeg2 import *

class Register:
  def __init__(self, name):
    self.name = name
    self.value = 0

def find_register(register, registers):
  return next((x for x in registers if x.name == register), None)

class Half:
  grammar = 'hlf', attr('register', word)

  def execute(self, registers):
    r = find_register(self.register, registers)
    r.value /= 2
    return 1

class Triple:
  grammar = 'tpl', attr('register', word)

  def execute(self, registers):
    r = find_register(self.register, registers)
    r.value *= 3
    return 1
  
class Increment:
  grammar = 'inc', attr('register', word)

  def execute(self, registers):
    r = find_register(self.register, registers)
    r.value += 1
    return 1
  
class Jump:
  grammar = 'jmp', attr('offset', restline)

  def execute(self, registers):
    return int(self.offset)

class JumpIfEven:
  grammar = 'jie', attr('register', word), ',', attr('offset', restline)

  def execute(self, registers):
    r = find_register(self.register, registers)
    if r.value % 2 == 0:
      return int(self.offset)
    return 1

class JumpIfOne:
  grammar = 'jio', attr('register', word), ',', attr('offset', restline)

  def execute(self, registers):
    r = find_register(self.register, registers)
    if r.value == 1:
      return int(self.offset)
    return 1
  
INSTRUCTIONS = [Half, Triple, Increment, Jump, JumpIfEven, JumpIfOne]

class Computer:
  def __init__(self, lines):
    self._registers = [Register('a'), Register('b')]
    self._instructions = []
    self._load_program(lines)

  def _load_program(self, lines):
    for line in lines:
      self._instructions.append(parse(line, INSTRUCTIONS))

  def run(self):
    i = 0
    while 0 <= i and i < len(self._instructions):
      i += self._instructions[i].execute(self._registers)

  def reset(self):
    for r in self._registers:
      r.value = 0

  def set_register(self, register, value):
    r = find_register(register, self._registers)
    r.value = value

  def get_register(self, register):
    r = find_register(register, self._registers)
    return r.value

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  computer = Computer(read_input())
  computer.run()
  print('Register b (part 1): %s' % computer.get_register('b'))
  computer.reset()
  computer.set_register('a', 1)
  computer.run()
  print('Register b (part 2): %s' % computer.get_register('b'))
