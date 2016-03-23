#!/usr/bin/env python3

import day17
import unittest

class TestDay17(unittest.TestCase):
  def test_containers(self):
    containers = [20, 15, 10, 5, 5]
    self.assertEqual(day17.store_eggnog(25, containers), 4)

if __name__ == '__main__':
  unittest.main()
