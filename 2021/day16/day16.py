#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
  result = ''
  for ch in raw_data[0]:
    result += '{0:04b}'.format(int(ch, 16))
  return result


class Packet:
  def __init__(self, data):
    self._version = int(data[0:3], 2)
    self._type = int(data[3:6], 2)
    self._length = 6
    self._literal = None
    self._subpackets = []
    if self._type == 4:
      self._parse_literal(data[6:])
    else:
      self._parse_subpackets(data[6:])

  def version(self):
    return self._version

  def packet_type(self):
    return self._type

  def _parse_literal(self, data):
    idx = 0
    result = ''
    while True:
      s = data[idx:idx+5]
      result += s[1:]
      self._length += 5
      if s[0] == '0':
        break
      idx += 5
    self._literal = int(result, 2)

  def literal(self):
    return self._literal

  def length(self):
    return self._length

  def _parse_subpackets(self, data):
    length_type = int(data[0])
    self._length += 1
    if length_type == 0:
      num_bits = int(data[1:16], 2)
      self._length += 15 + num_bits
      offset = 0
      while num_bits > 0:
        p = Packet(data[16+offset:])
        self._subpackets.append(p)
        offset += p.length()
        num_bits -= p.length()
    else:
      num_subpackets = int(data[1:12], 2)
      self._length += 11
      offset = 0
      while num_subpackets > 0:
        p = Packet(data[12+offset:])
        self._subpackets.append(p)
        self._length += p.length()
        offset += p.length()
        num_subpackets -= 1

  def sum_version(self):
    result = self._version
    for p in self._subpackets:
      result += p.sum_version()
    return result

  def value(self):
    if self._type == 0:
      return sum([p.value() for p in self._subpackets])
    if self._type == 1:
      product = 1
      for p in self._subpackets:
        product *= p.value()
      return product
    if self._type == 2:
      return min([p.value() for p in self._subpackets])
    if self._type == 3:
      return max([p.value() for p in self._subpackets])
    if self._type == 4:
      return self._literal
    if self._type == 5:
      return 1 if self._subpackets[0].value() > self._subpackets[1].value() else 0
    if self._type == 6:
      return 1 if self._subpackets[0].value() < self._subpackets[1].value() else 0
    if self._type == 7:
      return 1 if self._subpackets[0].value() == self._subpackets[1].value() else 0


def do_part1(data):
  packet = Packet(data)
  return packet.sum_version()


def do_part2(data):
  packet = Packet(data)
  return packet.value()


def execute():
  raw_data = read_data('input.txt')
  data = parse_data(raw_data)
  print('Part 1 answer:', do_part1(data))
  print('Part 2 answer:', do_part2(data))


if __name__ == '__main__':
  execute()
