#! /usr/bin/env python3

from collections import Counter


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Polymer:
  def __init__(self, raw_data):
    self._polymer = raw_data[0]
    self._rules = {(a := line.split(' -> '))[0]: a[1] for line in raw_data[2:]}

  def process(self, nsteps):
    pairs = Counter([a + b for (a, b) in zip(self._polymer, self._polymer[1:])])
    for n in range(nsteps):
      temp = Counter()
      for k, v in pairs.items():
        if k in self._rules:
          k1 = k[0] + self._rules[k]
          k2 = self._rules[k] + k[1]
          temp[k] -= v
          temp[k1] += v
          temp[k2] += v
      pairs += temp
    c = Counter()
    for k, v in pairs.items():
      c[k[0]] += v
      c[k[1]] += v
    c[self._polymer[0]] += 1
    c[self._polymer[-1]] += 1
    return (max(c.values()) - min(c.values())) // 2


def do_part1(raw_data):
  polymer = Polymer(raw_data)
  return polymer.process(10)


def do_part2(raw_data):
  polymer = Polymer(raw_data)
  return polymer.process(40)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
