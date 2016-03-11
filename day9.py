#!/usr/bin/env python3

import fileinput
import itertools

class Routes:
  def __init__(self, lines):
    self._cities = []
    self._distances = []
    for line in lines:
      line = line.split(' = ')
      cities = line[0].split(' to ')
      self._add_city(cities[0])
      self._add_city(cities[1])
      self._distances.append([cities[0], cities[1], int(line[1])])
      self._distances.append([cities[1], cities[0], int(line[1])])
    self._cities.sort()
    self._routes = list(itertools.permutations(self._cities, len(self._cities)))

  def _add_city(self, city):
    if not city in self._cities:
      self._cities.append(city)

  def get_lengths(self):
    lengths = []
    for route in self._routes:
      prev_city = ''
      length = 0
      for city in route:
        for dist in self._distances:
          if dist[0] == prev_city and dist[1] == city:
            length += dist[2]
        prev_city = city
      lengths.append(length)
    lengths.sort()
    return lengths

if __name__ == "__main__":
  lines = [line.rstrip() for line in fileinput.input()]
  routes = Routes(lines)
  lengths = routes.get_lengths()
  print("Min route length: %s" % lengths[0])
  print("Max route length: %s" % lengths[-1])
