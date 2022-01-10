#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Grid:
  def __init__(self, raw_data):
    self._grid = []
    for line in raw_data:
      self._grid.append([int(x) for x in line])
    self._nrows = len(self._grid)
    self._ncols = len(self._grid[0])

  def _flash_cell(self, r0, c0):
    for r in range(r0 - 1, r0 + 2):
      if r < 0 or r >= self._nrows:
        continue
      for c in range(c0 - 1, c0 + 2):
        if c < 0 or c >= self._ncols:
          continue
        if r == r0 and c == c0:
          continue
        self._increment_cell_level(r, c)

  def _increment_cell_level(self, r, c):
    if self._grid[r][c] <= 9:
      self._grid[r][c] += 1
      if self._grid[r][c] > 9:
        self._flash_cell(r, c)

  def _increment_all_levels(self):
    for r in range(0, self._nrows):
      for c in range(0, self._ncols):
        self._increment_cell_level(r, c)

  def _reset_energy_levels(self):
    cnt = 0
    for r in range(0, self._nrows):
      for c in range(0, self._ncols):
        if self._grid[r][c] > 9:
          self._grid[r][c] = 0
          cnt += 1
    return cnt

  def execute_steps(self, num):
    resets = 0
    for i in range(0, num):
      self._increment_all_levels()
      resets += self._reset_energy_levels()
    return resets

  def execute_until_all_flash(self):
    n = 1
    ncells = self._nrows * self._ncols
    while True:
      self._increment_all_levels()
      if self._reset_energy_levels() == ncells:
        return n
      n += 1


def do_part1(raw_data):
  grid = Grid(raw_data)
  return grid.execute_steps(100)


def do_part2(raw_data):
  grid = Grid(raw_data)
  return grid.execute_until_all_flash()


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
