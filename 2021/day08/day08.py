#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class SignalEntry:
  def __init__(self, raw_input):
    (term0, term1) = raw_input.split(' | ')
    self._signals = term0.split(' ')
    self._outputs = term1.split(' ')
    self._target_lengths = [2, 3, 4, 7]

  def easy_output_values(self):
    return [val for val in self._outputs if len(val) in self._target_lengths]

  def signals(self):
    return self._signals

  def outputs(self):
    return self._outputs


def parse_data(raw_data):
  return [SignalEntry(line) for line in raw_data]


def do_part1(raw_data):
  signal_entries = parse_data(raw_data)
  return sum(len(entry.easy_output_values()) for entry in signal_entries)

def do_part2(raw_data):
  signal_entries = parse_data(raw_data)
  count_mapping = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
  return sum(int("".join(str(count_mapping.index(sum(sig.count(val) for sig in entry.signals() for val in output))) for output in entry.outputs())) for entry in signal_entries)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
