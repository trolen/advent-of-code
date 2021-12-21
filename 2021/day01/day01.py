#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
  return [int(item) for item in raw_data]


def do_part1(depths):
  prev = None
  cnt = 0
  for depth in depths:
    if prev is not None and depth > prev:
      cnt += 1
    prev = depth
  return cnt


def do_part2(depths):
  n = len(depths) - 2
  sums = []
  for i in range(0, n):
    sums.append(sum(depths[i:i+3]))
  return do_part1(sums)


def execute():
  raw_data = read_data('input.txt')
  depths = parse_data(raw_data)
  print('Part 1 answer:', do_part1(depths))
  print('Part 2 answer:', do_part2(depths))


if __name__ == '__main__':
  execute()
