#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Grid:
  def __init__(self, raw_data):
    self._points = []
    self._folds = []
    first_section = True
    for line in raw_data:
      if len(line) == 0:
        first_section = False
        continue
      if first_section:
        (x, y) = [int(n) for n in line.split(',')]
        self._points.append((x, y))
      else:
        self._folds.append((line.split(' ')[-1].split('=')))

  def count_points(self):
    return len(self._points)

  def do_folds(self, stop_after_first_fold=True):
    for (dir, pos) in self._folds:
      pos = int(pos)
      new_points = []
      for (x, y) in self._points:
        if dir == 'x' and x > pos:
          x = pos - (x - pos)
        elif dir == 'y' and y > pos:
          y = pos - (y - pos)
        if (x, y) not in new_points:
          new_points.append((x, y))
      self._points = new_points
      if stop_after_first_fold:
        break

  def show_grid(self):
    max_x, max_y = -1, -1
    for (x, y) in self._points:
      max_x = max(x, max_x)
      max_y = max(y, max_y)
    for y in range(0, max_y + 1):
      for x in range(0, max_x + 1):
        ch = '*' if (x, y) in self._points else '.'
        print(ch, end='')
      print()


def do_part1(raw_data):
  grid = Grid(raw_data)
  grid.do_folds()
  return grid.count_points()


def do_part2(raw_data):
  grid = Grid(raw_data)
  grid.do_folds(stop_after_first_fold=False)
  grid.show_grid()
  return grid.count_points()


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
