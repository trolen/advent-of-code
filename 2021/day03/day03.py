#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def do_part1(data):
  n = len(data[0])
  gamma = ''
  epsilon = ''
  for i in range(0, n):
    bits = [item[i] for item in data]
    zeros = bits.count('0')
    ones = bits.count('1')
    gamma += '1' if ones > zeros else '0'
    epsilon += '0' if ones > zeros else '1'
  gamma = int(gamma, 2)
  epsilon = int(epsilon, 2)
  return gamma * epsilon


def filter_data(data, index):
  bits = [item[index] for item in data]
  zeros = bits.count('0')
  ones = bits.count('1')
  if ones >= zeros:
    gamma = [item for item in data if item[index] == '1']
    epsilon = [item for item in data if item[index] == '0']
  else:
    gamma = [item for item in data if item[index] == '0']
    epsilon = [item for item in data if item[index] == '1']
  return (gamma, epsilon)


def do_part2(data):
  n = len(data[0])
  o2_generator = data
  for i in range(0, n):
    (gamma, epsilon) = filter_data(o2_generator, i)
    o2_generator = gamma
    if len(o2_generator) == 1:
      break
  co2_scrubber = data
  for i in range(0, n):
    (gamma, epsilon) = filter_data(co2_scrubber, i)
    co2_scrubber = epsilon
    if len(co2_scrubber) == 1:
      break
  o2_generator = int(o2_generator[0], 2)
  co2_scrubber = int(co2_scrubber[0], 2)
  return o2_generator * co2_scrubber


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
