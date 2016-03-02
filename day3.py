#!/usr/bin/python3

import fileinput

class deliverer:
  def __init__(self, houses):
    self._houses = houses
    self._x = 0
    self._y = 0
    self._save_position()
  def _save_position(self):
    if [self._x,self._y] not in self._houses:
      self._houses.append([self._x,self._y])
  def move(self,c):
    if c == '^':
      self._y += 1
    if c == 'v':  
      self._y -= 1
    if c == '>':
      self._x += 1
    if c == '<':
      self._x -= 1
    self._save_position()

def year1(data):
  houses = []
  santa = deliverer(houses)
  for c in data:
    santa.move(c)
  return len(houses)

def year2(data):
  houses = []
  deliverers = [deliverer(houses), deliverer(houses)]
  toggle = 0
  for c in data:
    deliverers[toggle].move(c)
    toggle = 1 - toggle
  return len(houses)

if __name__ == "__main__":
  s = ''
  for line in fileinput.input():
    s += line
  print("Year 1, delivered to %s houses" % year1(s))
  print("Year 2, delivered to %s houses" % year2(s))
