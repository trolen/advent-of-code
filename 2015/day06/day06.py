#!/usr/bin/env python3

import fileinput
import re
import sys
import numpy as np
from pypeg2 import *

class Coord(List):
  grammar = int, ',', int

class Range(List):
  grammar = Coord, 'through', Coord

  def slice(self, lights):
    x1, y1 = self[0]
    x2, y2 = self[1]
    return lights[x1:x2+1, y1:y2+1]

  def apply(self, lights, f):
    l = self.slice(lights)
    l[:] = f(l)

class Toggle:
  grammar = 'toggle', attr('range', Range)

  def part1(self, lights):
    self.range.apply(lights, lambda l: 1 - l)

  def part2(self, lights):
    self.range.apply(lights, lambda l: l + 2)

class TurnOff:
  grammar = 'turn off', attr('range', Range)

  def part1(self, lights):
    self.range.apply(lights, lambda l: 0)

  def part2(self, lights):
    self.range.apply(lights, lambda l: np.fmax(l - 1, 0))

class TurnOn:
  grammar = 'turn on', attr('range', Range)

  def part1(self, lights):
    self.range.apply(lights, lambda l: 1)

  def part2(self, lights):
    self.range.apply(lights, lambda l: l + 1)

commands = [Toggle, TurnOff, TurnOn]

def make_grid():
  return np.zeros((1000, 1000), dtype=int)

def parse_line(line):
  return parse(line, commands)

def grid_sum(grid):
  return np.sum(grid)

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lights1 = make_grid()
  lights2 = make_grid()
  
  lines = read_input()
  for line in lines:
    cmd = parse_line(line)
    cmd.part1(lights1)
    cmd.part2(lights2)

  print("Lights lit (part 1): %s" % grid_sum(lights1))
  print("Total brightness (part 2): %s" % grid_sum(lights2))
