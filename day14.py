#!/usr/bin/env python3

import fileinput
import sys

class Race:
  def __init__(self, lines):
    self._deer = []
    for line in lines:
      words = line.split(' ')
      name = words[0]
      speed = int(words[3])
      flight_time = int(words[6])
      rest_time = int(words[-2])
      self._deer.append({"name":name, "speed":speed, "flight_time":flight_time,
                         "rest_time":rest_time, "in_flight":True,
                         "time_count":0, "distance":0, "points":0})

  def _accumulate_distance(self):
    for deer in self._deer:
      end_count = deer["rest_time"]
      if deer["in_flight"]:
        deer["distance"] += deer["speed"]
        end_count = deer["flight_time"]
      deer["time_count"] += 1
      if deer["time_count"] >= end_count:
        deer["in_flight"] = not deer["in_flight"]
        deer["time_count"] = 0

  def _award_points(self):
    max_distance = self.max_distance()
    for deer in self._deer:
      if deer["distance"] == max_distance:
        deer["points"] += 1

  def run(self, sec_to_run):
    for x in range(sec_to_run):
      self._accumulate_distance()
      self._award_points()

  def max_distance(self):
    return max([deer["distance"] for deer in self._deer])

  def max_points(self):
    return max([deer["points"] for deer in self._deer])

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  race = Race(lines)
  race.run(2503)
  print("Max distance: %s" % race.max_distance())
  print("Max points: %s" % race.max_points())
