#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
  return [int(x) for x in raw_data[0].split(',')]


def simulate(raw_data, num_days):
  data = parse_data(raw_data)
  fish = [0] * 9
  for i in data:
    fish[i] += 1
  for i in range(num_days):
    x = fish[0]
    fish = fish[1:] + [x]
    fish[6] += x
  return sum(fish)


def do_part1(raw_data):
  return simulate(raw_data, 80)


def do_part2(raw_data):
  return simulate(raw_data, 256)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
