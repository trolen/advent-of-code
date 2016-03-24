#!/usr/bin/env python3

import fileinput
import sys

def count_neighbors(grid, x, y):
  count = 0
  x1 = x - 1 if x > 0 else x
  y1 = y - 1 if y > 0 else y
  x2 = x + 1 if x < len(grid)-1 else x
  y2 = y + 1 if y < len(grid[x])-1 else y
  for i in range(x1, x2+1):
    for j in range(y1, y2+1):
      if i == x and j == y:
        continue
      if grid[i][j] == '#':
        count += 1
  return count

def animate_lights(grid, num_steps, corners_on):
  if corners_on:
    grid[0] = '#' + grid[0][1:-1] + '#'
    grid[-1] = '#' + grid[-1][1:-1] + '#'
  len_x = len(grid)
  len_y = len(grid[0])
  old_grid = grid
  new_grid = None
  for n in range(num_steps):
    new_grid = []
    for i in range(len_x):
      row = ''
      for j in range(len_y):
        if corners_on and i in [0, len_x-1] and j in [0, len_y-1]:
          row += '#'
          continue
        c = count_neighbors(old_grid, i, j)
        if old_grid[i][j] == '#':
          row += '#' if c in [2,3] else '.'
        else:
          row += '#' if c == 3 else '.'
      new_grid.append(row)
    old_grid = new_grid
  return new_grid

def count_lights_on(grid):
  return sum(x.count('#') for x in grid)

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  lights = animate_lights(lines, 100, False)
  print("Lights on: %s" % count_lights_on(lights))
  lights = animate_lights(lines, 100, True)
  print("Lights with corners on: %s" % count_lights_on(lights))
