#! /usr/bin/env python3

import heapq


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Network:
  def __init__(self, raw_data, size_multiplier=1):
    self._risks = self._build_risks(raw_data, size_multiplier)
    self._nrows = len(self._risks)
    self._ncols = len(self._risks[0])
    self._costs = [[-1] * self._ncols for i in range(self._nrows)]
    self._costs[0][0] = 0

  def _build_risks(self, raw_data, size_multiplier):
    risks = []
    for line in raw_data:
      row = [int(ch) for ch in line]
      ncols = len(row)
      for i in range(1, size_multiplier):
        for c in range(ncols):
          row.append((row[c] + i - 1) % 9 + 1)
      risks.append(row)
    nrows = len(risks)
    ncols = len(risks[0])
    for i in range(1, size_multiplier):
      for r in range(nrows):
        row = []
        for c in range(ncols):
          row.append((risks[r][c] + i - 1) % 9 + 1)
        risks.append(row)
    return risks

  def find_lowest_cost(self):
    risk_counter = {(0, 0): 0}
    need_checks = [(0, (0, 0))]
    while len(need_checks) > 0:
      risk, (r, c) = heapq.heappop(need_checks)
      if risk <= risk_counter[(r, c)]:
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
          r1 = r + dr
          c1 = c + dc
          if 0 <= r1 < self._nrows and 0 <= c1 < self._ncols:
            pos_risk = risk + self._risks[r1][c1]
            if pos_risk < risk_counter.get((r1, c1), 2 ** 32):
              risk_counter[(r1, c1)] = pos_risk
              heapq.heappush(need_checks, (pos_risk, (r1, c1)))
    return risk_counter[(self._nrows - 1, self._ncols - 1)]


def do_part1(raw_data):
  network = Network(raw_data)
  return network.find_lowest_cost()


def do_part2(raw_data):
  network = Network(raw_data, size_multiplier=5)
  return network.find_lowest_cost()


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
