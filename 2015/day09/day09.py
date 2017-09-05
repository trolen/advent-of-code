#!/usr/bin/env python3

import fileinput
import itertools
import sys

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
    self._build_routes()

  def _add_city(self, city):
    if not city in self._cities:
      self._cities.append(city)

  def _build_routes(self):
    self._routes = list(itertools.permutations(self._cities, len(self._cities)))
    self._lengths = []
    for route in self._routes:
      prev_city = ''
      length = 0
      for city in route:
        for dist in self._distances:
          if dist[0] == prev_city and dist[1] == city:
            length += dist[2]
        prev_city = city
      self._lengths.append(length)
    self._lengths.sort()

  def get_shortest_length(self):
    return self._lengths[0]

  def get_longest_length(self):
    return self._lengths[-1]

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  routes = Routes(lines)
  print("Min route length: %s" % routes.get_shortest_length())
  print("Max route length: %s" % routes.get_longest_length())
