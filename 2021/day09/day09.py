#! /usr/bin/env python3

import math


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Grid:
  def __init__(self, raw_data):
    self._grid = []
    for line in raw_data:
      self._grid.append([int(c) for c in line])

  def _get_low_points(self):
    points = []
    nrows = len(self._grid)
    for r in range(0, nrows):
      ncols = len(self._grid[r])
      for c in range(0, ncols):
        x = self._grid[r][c]
        if r > 0 and x >= self._grid[r - 1][c]:
          continue
        if c > 0 and x >= self._grid[r][c - 1]:
          continue
        if r < nrows - 1 and x >= self._grid[r + 1][c]:
          continue
        if c < ncols - 1 and x >= self._grid[r][c + 1]:
          continue
        points.append((r, c))
    return points

  def _get_basin_points(self, r, c):
    nrows = len(self._grid)
    ncols = len(self._grid[0])
    x = self._grid[r][c]
    points = [(r, c)]
    if r > 0 and x < self._grid[r - 1][c] < 9:
      points += self._get_basin_points(r - 1, c)
    if c > 0 and x < self._grid[r][c - 1] < 9:
      points += self._get_basin_points(r, c - 1)
    if r < nrows - 1 and x < self._grid[r + 1][c] < 9:
      points += self._get_basin_points(r + 1, c)
    if c < ncols - 1 and x < self._grid[r][c + 1] < 9:
      points += self._get_basin_points(r, c + 1)
    return points

  def part1(self):
    low_points = self._get_low_points()
    return sum([self._grid[r][c] for (r,c) in low_points]) + len(low_points)

  def part2(self):
    low_points = self._get_low_points()
    basin_sizes = []
    for (r, c) in low_points:
      basin_sizes.append(len(list(dict.fromkeys(self._get_basin_points(r, c)))))
    basin_sizes.sort(reverse=True)
    return math.prod(basin_sizes[:3])


def do_part1(raw_data):
  grid = Grid(raw_data)
  return grid.part1()


def do_part2(raw_data):
  grid = Grid(raw_data)
  return grid.part2()


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
