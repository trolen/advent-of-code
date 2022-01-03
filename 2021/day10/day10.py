#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class NavLine:
  def __init__(self, raw_line):
    self._line = raw_line
    self._opening_chars = '([{<'
    self._closing_chars = ')]}>'
    self._closing_points = [1, 2, 3, 4]
    self._error_points = [3, 57, 1197, 25137]
    self._closing_score = 0
    self._error_score = 0
    self._calc_scores()

  def _calc_scores(self):
    chunks = []
    for ch in self._line:
      if ch in self._opening_chars:
        chunks.append(ch)
        continue
      idx = self._closing_chars.index(ch)
      if self._opening_chars[idx] == chunks[-1]:
        chunks = chunks[:-1]
        continue
      self._error_score = self._error_points[idx]
      return
    n = len(chunks)
    for i in range(0, n):
      idx = self._opening_chars.index(chunks[-1])
      self._closing_score = self._closing_score * 5 + self._closing_points[idx]
      chunks = chunks[:-1]


  def closing_score(self):
    return self._closing_score

  def error_score(self):
    return self._error_score


def do_part1(raw_data):
  scores = []
  for raw_line in raw_data:
    line = NavLine(raw_line)
    scores.append(line.error_score())
  return sum(scores)


def do_part2(raw_data):
  scores = []
  for raw_line in raw_data:
    line = NavLine(raw_line)
    score = line.closing_score()
    if score > 0:
      scores.append(score)
  scores.sort()
  return scores[int(len(scores) / 2)]


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
