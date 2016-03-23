#!/usr/bin/env python3

import fileinput
import sys

class Recipe:
  def __init__(self, lines):
    self._ingredients = []
    for line in lines:
      words = line.split(' ')
      name = words[0][:-1]
      cap = int(words[2][:-1])
      dur = int(words[4][:-1])
      fla = int(words[6][:-1])
      tex = int(words[8][:-1])
      cal = int(words[10])
      self._ingredients.append({"name":name, "capacity":cap, "durability":dur,
                                "flavor":fla, "texture":tex, "calories":cal})

  def build_ratios(self, max_amount):
    num_ingredients = len(self._ingredients)
    amounts = [0] * num_ingredients
    self._ratios = []
    while sum(amounts) < num_ingredients * max_amount:
      for i in range(num_ingredients):
        amounts[i] += 1
        if amounts[i] > max_amount:
          amounts[i] = 0
        else:
          break
      if sum(amounts) == max_amount:
        self._ratios.append(amounts[:])

  def max_score(self, calories):
    result = 0
    for r in self._ratios:
      cal = 0
      cap = 0
      dur = 0
      fla = 0
      tex = 0
      for i in range(len(r)):
        cal += self._ingredients[i]["calories"] * r[i]
        cap += self._ingredients[i]["capacity"] * r[i]
        dur += self._ingredients[i]["durability"] * r[i]
        fla += self._ingredients[i]["flavor"] * r[i]
        tex += self._ingredients[i]["texture"] * r[i]
        i += 1
      cap = cap if cap > 0 else 0
      dur = dur if dur > 0 else 0
      fla = fla if fla > 0 else 0
      tex = tex if tex > 0 else 0
      score = cap * dur * fla * tex
      if calories > 0 and cal != calories:
        continue
      result = max(result, score)
    return result

def read_input():
  if len(sys.argv) < 2:
    print("Input file name missing")
    sys.exit(1)
  return [line.rstrip() for line in fileinput.input()]

if __name__ == "__main__":
  lines = read_input()
  recipe = Recipe(lines)
  recipe.build_ratios(100)
  print("Max score: %s" % recipe.max_score(0))
  print("Max score (500 calories): %s" % recipe.max_score(500))
