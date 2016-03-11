#!/usr/bin/env python3

import day9
import unittest

class TestDay9(unittest.TestCase):
  def test_lengths(self):
    lines = ['London to Dublin = 464',
      'London to Belfast = 518',
      'Dublin to Belfast = 141']
    routes = day9.Routes(lines)
    self.assertEqual(routes.get_shortest_length(), 605)
    self.assertEqual(routes.get_longest_length(), 982)

if __name__ == '__main__':
  unittest.main()
