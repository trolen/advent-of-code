#!/usr/bin/python

import fileinput

class house_grid:
  def __init__(self):
    self._houses = []
  def deliver_to(self, x, y):
    for house in self._houses:
      if house[0] == x and house[1] == y:
        house[2] += 1
        return
    self._houses.append([x, y, 1])
  def house_count(self):
    return len(self._houses)

class deliverer:
  def __init__(self):
    self._x = 0
    self._y = 0
  def north(self):
    self._y += 1
  def south(self):
    self._y -= 1
  def east(self):
    self._x += 1
  def west(self):
    self._x -= 1
  def deliver_to(self, grid):
    grid.deliver_to(self._x, self._y)

def year1(data):
  houses = house_grid()
  santa = deliverer()
  santa.deliver_to(houses)
  for c in data:
    if c == '<':
      santa.east()
      santa.deliver_to(houses)
    if c == '>':
      santa.west()
      santa.deliver_to(houses)
    if c == '^':
      santa.north()
      santa.deliver_to(houses)
    if c == 'v':
      santa.south()
      santa.deliver_to(houses)
  return houses.house_count()

def year2(data):
  houses = house_grid()
  deliverers = [deliverer(), deliverer()]
  deliverers[0].deliver_to(houses)
  toggle = 0
  for c in data:
    if c == '<':
      deliverers[toggle].east()
      deliverers[toggle].deliver_to(houses)
    if c == '>':
      deliverers[toggle].west()
      deliverers[toggle].deliver_to(houses)
    if c == '^':
      deliverers[toggle].north()
      deliverers[toggle].deliver_to(houses)
    if c == 'v':
      deliverers[toggle].south()
      deliverers[toggle].deliver_to(houses)
    toggle = 1 - toggle
  return houses.house_count()

if __name__ == "__main__":
  s = fileinput.input()[0]
  print "Year 1, delivered to", year1(s), "houses"
  print "Year 2, delivered to", year2(s), "houses"
