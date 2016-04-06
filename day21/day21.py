#!/usr/bin/env python3

class Player:
  def __init__(self, hit_points, damage, armor):
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
      return 'Player'
    if take_turn(boss, player):
      return 'Boss'

if __name__ == "__main__":
  boss = Player(104, 8, 1)
  player = Player(100, 11, 8)
  winner = play_game(boss, player)
  print("%s wins" % winner)
