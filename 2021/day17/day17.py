#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Probe:
  def __init__(self, raw_data):
    self._xmin, self._xmax, self._ymin, self._ymax = self._parse_data(raw_data)

  def _parse_data(self, raw_data):
    xrange, yrange = raw_data[0].split(': ')[1].split(', ')
    xmin, xmax = (int(s) for s in xrange.split('=')[1].split('..'))
    ymin, ymax = (int(s) for s in yrange.split('=')[1].split('..'))
    return (xmin, xmax, ymin, ymax)

  def target_area(self):
    return (self._xmin, self._xmax), (self._ymin, self._ymax)

  def fire_probe(self, velx, vely):
    posx = posy = 0
    hit_target = False
    while True:
      if self._xmin <= posx <= self._xmax and self._ymin <= posy <= self._ymax:
        hit_target = True
        break
      if posx > self._xmax or posy < self._ymin:
        break
      posx += velx
      posy += vely
      velx = velx - 1 if velx > 0 else 0
      vely = vely - 1
    return hit_target


def do_part1(raw_data):
  probe = Probe(raw_data)
  xrange, yrange = probe.target_area()
  ymin = abs(yrange[0])
  return ymin * (ymin - 1) // 2


def do_part2(raw_data):
  probe = Probe(raw_data)
  (xmin, xmax), (ymin, ymax) = probe.target_area()
  count = 0
  for velx in range(1, xmax + 1):
    for vely in range(ymin, abs(ymin)):
      if probe.fire_probe(velx, vely):
        count += 1
  return count


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
