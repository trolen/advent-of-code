#!/usr/bin/env python3

import day15
import unittest

class TestDay15(unittest.TestCase):
  def test_recipe(self):
    lines = ['Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
             'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']
    recipe = day15.Recipe(lines)
    recipe.build_ratios(100)
    self.assertEqual(recipe.max_score(0), 62842880)
    self.assertEqual(recipe.max_score(500), 57600000)

if __name__ == '__main__':
  unittest.main()
