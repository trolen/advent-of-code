#!/usr/bin/env python3

import fileinput
import re

def parse_line(line):
  pattern = re.compile(r'(?P<cmd>turn on|turn off|toggle)\s(?P<x1>\d+),(?P<y1>\d+)\sthrough\s(?P<x2>\d+),(?P<y2>\d+)')
  match = pattern.match(line)
  command = match.group('cmd')
  x1 = int(match.group('x1'))
  y1 = int(match.group('y1'))
  x2 = int(match.group('x2'))
  y2 = int(match.group('y2'))
  return (command, x1, y1, x2, y2)

def grid_iter(lines):
  for line in lines:
    (command, x1, y1, x2, y2) = parse_line(line)
    for x in range(x1, x2+1):
      for y in range(y1, y2+1):
        yield (command, x, y)

def grid_sum(grid):
  grid_sum = 0
  for row in grid:
    grid_sum += sum(row)
  return grid_sum

def set_lights1(lines):
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  for (command, x, y) in grid_iter(lines):
    if command == 'turn off':
      light_grid[x][y] = 0
    if command == 'turn on':
      light_grid[x][y] = 1
    if command == 'toggle':
      light_grid[x][y] = 1 - light_grid[x][y]
  return grid_sum(light_grid)

def set_lights2(lines):
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  for (command, x, y) in grid_iter(lines):
    if command == 'turn off' and light_grid[x][y] > 0:
      light_grid[x][y] -= 1
    if command == 'turn on':
      light_grid[x][y] += 1
    if command == 'toggle':
      light_grid[x][y] += 2
  return grid_sum(light_grid)

if __name__ == "__main__":
  lines = [x.rstrip() for x in fileinput.input()]
  print("Lights lit (method #1): %s" % set_lights1(lines))
  print("Total brightness (method #2): %s" % set_lights2(lines))
