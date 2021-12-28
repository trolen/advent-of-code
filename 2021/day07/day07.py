#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
  return [int(x) for x in raw_data[0].split(',')]


def formula1(x1, x2):
  return x1 - x2 if x1 > x2 else x2 - x1


def formula2(x1, x2):
  dx = formula1(x1, x2)
  return sum([i for i in range(1, dx + 1)])


def calc_costs(data, alt_formula=False):
  x0 = min(data)
  x1 = max(data)
  positions = [x0 + i for i in range(0, x1 - x0 + 1)]
  costs = []
  for x in positions:
    cost = 0
    for n in data:
      cost += formula1(n, x) if not alt_formula else formula2(n, x)
    costs.append(cost)
  return min(costs)


def do_part1(raw_data):
  data = parse_data(raw_data)
  return calc_costs(data)

def do_part2(raw_data):
  data = parse_data(raw_data)
  return calc_costs(data, alt_formula=True)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
