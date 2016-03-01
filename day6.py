#!/usr/bin/python

INPUT_FILE="day6_input.txt"

def read_input_file():
  lines = []
  with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
  return lines

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

def set_lights1():
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  lines = read_input_file()
  for line in lines:
    line = line.rstrip()
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

def set_lights2():
  light_grid = [[0 for x in range(1000)] for x in range(1000)]
  lines = read_input_file()
  for line in lines:
    line = line.rstrip()
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
  print "Lights lit (method #1):", set_lights1()
  print "Total brightness (method #2):", set_lights2()
