#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Line:
  def __init__(self, raw_line):
    raw_points = raw_line.split(' -> ')
    (self._x1, self._y1) = (int(x) for x in raw_points[0].split(','))
    (self._x2, self._y2) = (int(x) for x in raw_points[1].split(','))

  def is_vertical(self):
    return self._x1 == self._x2

  def is_horizontal(self):
    return self._y1 == self._y2

  def get_points(self):
    points = []
    n = self._x2 - self._x1
    if n == 0:
      n = self._y2 - self._y1
    n = abs(n) + 1
    dx = 1
    if self.is_vertical():
      dx = 0
    elif self._x1 > self._x2:
      dx = -1
    dy = 1
    if self.is_horizontal():
      dy = 0
    elif self._y1 > self._y2:
      dy = -1
    for i in range(0, n):
      points.append((self._x1 + i * dx, self._y1 + i * dy))
    return points

class Grid:
  def __init__(self):
    self._grid = []

  def mark_point(self, x, y):
    nrows = len(self._grid)
    ncols = 0
    if nrows > 0:
      ncols = len(self._grid[0])
    if x >= ncols:
      for r in range(0, nrows):
        for c in range(ncols, x + 1):
          self._grid[r].append(0)
      ncols = x + 1
    if y >= nrows:
      for r in range(nrows, y + 1):
        self._grid.append([0] * ncols)
    self._grid[y][x] = self._grid[y][x] + 1

  def num_overlap_points(self):
    cnt = 0
    for row in self._grid:
      for val in row:
        if val > 1:
          cnt += 1
    return cnt


def parse_lines(raw_data):
  lines = []
  for raw_line in raw_data:
    lines.append(Line(raw_line))
  return lines


def do_part1(raw_data):
  lines = parse_lines(raw_data)
  grid = Grid()
  for line in lines:
    if line.is_horizontal() or line.is_vertical():
      for (x, y) in line.get_points():
        grid.mark_point(x, y)
  return grid.num_overlap_points()


def do_part2(raw_data):
  lines = parse_lines(raw_data)
  grid = Grid()
  for line in lines:
    for (x, y) in line.get_points():
      grid.mark_point(x, y)
  return grid.num_overlap_points()


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
