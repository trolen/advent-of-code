#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]

def parse_data(raw_data):
  return [int(item) for item in raw_data]

def do_part1(entries):
  for i in range(0, len(entries) - 1):
    x = entries[i]
    for j in range(i + 1, len(entries)):
      y = entries[j]
      n = x + y
      if n == 2020:
        return x * y
  return 0

def do_part2(entries):
  for i in range(0, len(entries) - 2):
    x = entries[i]
    for j in range(i + 1, len(entries) - 1):
      y = entries[j]
      for k in range(j + 1, len(entries)):
        z = entries[k]
        n = x + y + z
        if n == 2020:
          return x * y * z
  return 0

def execute():
  raw_data = read_data('input.txt')
  entries = parse_data(raw_data)
  print('Part 1 answer:', do_part1(entries))
  print('Part 2 answer:', do_part2(entries))

if __name__ == '__main__':
  execute()