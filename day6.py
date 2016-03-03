#!/usr/bin/env python3

import fileinput

def get_command(line):
  if line.startswith('turn off'):
    return 0
  if line.startswith('turn on'):
    return 1
  if line.startswith('toggle'):
    return 2
  return -1

def get_start(line):
  words = line.split(',')
  x = words[0].split(' ')[-1]
  y = words[1].split(' ')[0]
  return int(x), int(y)

def get_end(line):
  words = line.split(',')
  x = words[1].split(' ')[-1]
  y = words[2].split(' ')[0]
  return int(x), int(y)

def set_lights1(lines):
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  for line in lines:
    command = get_command(line)
    startx, starty = get_start(line)
    endx, endy = get_end(line)
    for x in range(startx, endx+1):
      for y in range(starty, endy+1):
        if command == 0:
          light_grid[x][y] = 0
        if command == 1:
          light_grid[x][y] = 1
        if command == 2:
          light_grid[x][y] = 1 - light_grid[x][y]
  light_count = 0
  for i in light_grid:
    for j in i:
      if j > 0:
        light_count += 1
  return light_count

def set_lights2(lines):
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  for line in lines:
    command = get_command(line)
    startx, starty = get_start(line)
    endx, endy = get_end(line)
    for x in range(startx, endx+1):
      for y in range(starty, endy+1):
        if command == 0 and light_grid[x][y] > 0:
          light_grid[x][y] -= 1
        if command == 1:
          light_grid[x][y] += 1
        if command == 2:
          light_grid[x][y] += 2
  brightness = 0
  for i in light_grid:
    for j in i:
      brightness += j
  return brightness

if __name__ == "__main__":
  lines = [x.rstrip() for x in fileinput.input()]
  print("Lights lit (method #1): %s" % set_lights1(lines))
  print("Total brightness (method #2): %s" % set_lights2(lines))
