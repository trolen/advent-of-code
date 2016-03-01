#!/usr/bin/python

import itertools

INPUT_FILE="day9_input.txt"

all_cities = []
distances = []

def add_city(city):
  global all_cities
  for c in all_cities:
    if c == city:
      return
  all_cities.append(city)

def read_distances():
  global all_cities
  global distances
  with open(INPUT_FILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
      line = line.rstrip().split(' = ')
      cities = line[0].split(' to ')
      add_city(cities[0])
      add_city(cities[1])
      distances.append([cities[0], cities[1], int(line[1])])
      distances.append([cities[1], cities[0], int(line[1])])
  all_cities.sort()

def build_routes(cities):
  return list(itertools.permutations(cities, len(cities)))

def get_lengths(routes):
  global distances
  lengths = []
  for route in routes:
    prev_city = ''
    length = 0
    for city in route:
      for dist in distances:
        if dist[0] == prev_city and dist[1] == city:
          length += dist[2]
      prev_city = city
    lengths.append(length)
  lengths.sort()
  return lengths

if __name__ == "__main__":
  read_distances()
  routes = build_routes(all_cities)
  lengths = get_lengths(routes)
  print "Min length:", lengths[0]
  print "Max length:", lengths[-1]
