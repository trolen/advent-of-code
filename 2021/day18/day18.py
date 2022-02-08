#! /usr/bin/env python3

import sys
from itertools import combinations


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Pair:
  def __init__(self, raw_input=None):
    self._elements = []
    self._num_chars = 0
    if raw_input is None:
      return
    self._parse_err_msg = 'ERROR: Invalid character'
    if raw_input[0] != '[':
      sys.exit(self._parse_err_msg)
    self._num_chars += 1
    self._parse_element(raw_input[self._num_chars:])
    if raw_input[self._num_chars] != ',':
      sys.exit(self._parse_err_msg)
    self._num_chars += 1
    self._parse_element(raw_input[self._num_chars:])
    if raw_input[self._num_chars] != ']':
      sys.exit(self._parse_err_msg)
    self._num_chars += 1

  def _parse_element(self, input_str):
    if input_str[0] == '[':
      self._elements.append(Pair(input_str))
      self._num_chars += self._elements[-1].num_chars_parsed()
    elif input_str[0].isdigit():
      s = ''
      for ch in input_str:
        if not ch.isdigit():
          break
        s += ch
      self._elements.append(int(s))
      self._num_chars += len(s)
    else:
      sys.exit(self._parse_err_msg)

  def num_chars_parsed(self):
    return self._num_chars

  def __add__(self, other):
    result = Pair()
    result._elements = [self, other]
    return result

  def __eq__(self, other):
    if other is None:
      return False
    l1 = len(self._elements)
    l2 = len(other._elements)
    if l1 == 0 and l2 == 0:
      return True
    if l1 != 2 or l2 != 2:
      return False
    if type(self._elements[0]) == type(other._elements[0]) and self._elements[0] == other._elements[0]:
      return type(self._elements[1]) == type(other._elements[1]) and self._elements[1] == other._elements[1]
    return False

  def elements(self):
    return self._elements

  def _add_exploded_value(self, idx, side, value):
    if not isinstance(self._elements[idx], Pair):
      self._elements[idx] += value
      return
    self._elements[idx]._add_exploded_value(side, side, value)

  def _explode(self, nest_level=0):
    n = len(self._elements)
    for i in range(0, n):
      if isinstance(self._elements[i], Pair):
        if nest_level == 3:
          values = self._elements[i].elements()
          self._elements[i] = 0
          j = 1 - i
          self._add_exploded_value(j, i, values[j])
          values[j] = -1
          return True, values
        did_explode, values = self._elements[i]._explode(nest_level+1)
        if did_explode:
          j = 1 - i
          if values[j] > -1:
            self._add_exploded_value(j, i, values[j])
            values[j] = -1
          return True, values
    return False, []

  def _split(self):
    n = len(self._elements)
    for i in range(0, n):
      if isinstance(self._elements[i], Pair):
        if self._elements[i]._split():
          return True
      elif self._elements[i] >= 10:
        e0 = self._elements[i]
        e1 = e0 // 2
        e2 = e1 + e0 % 2
        p = Pair()
        p._elements = [e1, e2]
        self._elements[i] = p
        return True
    return False

  def reduce(self):
    while True:
      did_explode, _ = self._explode()
      if did_explode:
        continue
      if self._split():
        continue
      break

  def magnitude(self):
    if len(self._elements) == 0:
      return 0
    m0 = self._elements[0]
    if isinstance(m0, Pair):
      m0 = m0.magnitude()
    m1 = self._elements[1]
    if isinstance(m1, Pair):
      m1 = m1.magnitude()
    return 3 * m0 + 2 * m1


class Homework:
  def __init__(self, raw_data):
    self._pairs = [Pair(line) for line in raw_data]

  def part1(self):
    result = self._pairs[0]
    for num in self._pairs[1:]:
      result = result + num
      result.reduce()
    return result.magnitude()


def do_part1(raw_data):
  homework = Homework(raw_data)
  return homework.part1()


def do_part2(raw_data):
  return max(max(do_part1(i), do_part1(i[::-1])) for i in combinations(raw_data, 2))


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
