#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
  commands = []
  for command in [item.split() for item in raw_data]:
    cmd = command[0]
    n = int(command[1])
    commands.append([cmd, n])
  return commands


def do_part1(commands):
  depth = 0
  pos = 0
  for command in commands:
    (cmd, n) = command
    if cmd == 'forward':
      pos += n
    elif cmd == 'down':
      depth += n
    elif cmd == 'up':
      depth -= n
  return pos * depth


def do_part2(commands):
  depth = 0
  pos = 0
  aim = 0
  for command in commands:
    (cmd, n) = command
    if cmd == 'forward':
      pos += n
      depth += (aim * n)
    elif cmd == 'down':
      aim += n
    elif cmd == 'up':
      aim -= n
  return pos * depth


def execute():
  raw_data = read_data('input.txt')
  commands = parse_data(raw_data)
  print('Part 1 answer:', do_part1(commands))
  print('Part 2 answer:', do_part2(commands))


if __name__ == '__main__':
  execute()
