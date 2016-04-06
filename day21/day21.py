#!/usr/bin/env python3

class Player:
  def __init__(self, hit_points, damage, armor):
    self.reset(hit_points, damage, armor)

  def reset(self, hit_points, damage, armor):
    self.hit_points = hit_points
    self.damage = damage
    self.armor = armor

def take_turn(attacker, defender):
  defender.hit_points -= max(1, attacker.damage - defender.armor)
  if defender.hit_points <= 0:
    return True
  return False

def play_game(boss, player):
  while True:
    if take_turn(player, boss):
      return True
    if take_turn(boss, player):
      return False

class Tool:
  def __init__(self, name, cost, damage, armor):
    self.name = name
    self.cost = cost
    self.damage = damage
    self.armor = armor

WEAPONS = [Tool('Dagger', 8, 4, 0),
           Tool('Shortsword', 10, 5, 0),
           Tool('Warhammer', 25, 6, 0),
           Tool('Longsword', 40, 7, 0),
           Tool('Greataxe', 74, 8, 0)]

ARMOR = [Tool('Leather', 13, 0, 1),
         Tool('Chainmail', 31, 0, 2),
         Tool('Splitmail', 53, 0, 3),
         Tool('Bandemail', 75, 0, 4),
         Tool('Platemail', 102, 0, 5)]

RINGS = [Tool('Damage +1', 25, 1, 0),
         Tool('Damage +2', 50, 2, 0),
         Tool('Damage +3', 100, 3, 0),
         Tool('Defense +1', 20, 0, 1),
         Tool('Defense +2', 40, 0, 2),
         Tool('Defense +3', 80, 0, 3)]

def iter_armor():
  yield 0, 0, 0
  for a in ARMOR:
    yield a.cost, a.damage, a.armor

def iter_rings():
  yield 0, 0, 0
  for r in RINGS:
    yield r.cost, r.damage, r.armor
  for i in range(len(RINGS) - 1):
    r1 = RINGS[i]
    for j in range(i + 1, len(RINGS)):
      r2 = RINGS[j]
      yield r1.cost + r2.cost, r1.damage + r2.damage, r1.armor + r2.armor

def iter_player_stats():
  for w in WEAPONS:
    for a in iter_armor():
      for r in iter_rings():
        yield w.cost + a[0] + r[0], w.damage + a[1] + r[1], w.armor + a[2] + r[2]

if __name__ == "__main__":
  boss = Player(0, 0, 0)
  player = Player(0, 0, 0)
  costs = []
  for stats in iter_player_stats():
    boss.reset(104, 8, 1)
    player.reset(100, stats[1], stats[2])
    if play_game(boss, player):
      costs.append(stats[0])
  print("Minimum cost to win: %s" % min(costs))
  costs = []
  for stats in iter_player_stats():
    boss.reset(104, 8, 1)
    player.reset(100, stats[1], stats[2])
    if not play_game(boss, player):
      costs.append(stats[0])
  print("Maximum cost to lose: %s" % max(costs))
