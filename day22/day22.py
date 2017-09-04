#!/usr/bin/env python3

class Wizard:
  def __init__(self, hit_points, mana):
    self.reset(hit_points, mana)

  def reset(self, hit_points, mana):
    self.hit_points = hit_points
    self.mana = mana
    self.armor = 0

class Boss:
  def __init__(self, hit_points, damage):
    self.reset(hit_points, damage)

  def reset(self, hit_points, damage):
    self.hit_points = hit_points
    self.damage = damage
    self.armor = 0

class Spell:
  def __init__(self, name, cost, effect, damage, heal, armor, mana):
    self.name = name
    self.cost = cost
    self.effect = effect
    self.damage = damage
    self.heal = heal
    self.armor = armor
    self.mana = mana
    self.timer = 0

  def buy(self, player, boss):
      player.mana -= self.cost
      if self.effect == 0:
          if self.damage > 0:
              boss.hit_points -= self.damage
          if self.heal > 0:
              player.hit_points += self.heal

  def apply_effect(self, player, boss):
      if self.effect > 0 and self.timer > 0:
          if self.damage > 0:
              boss.hit_points -= spell.damage
          if self.armor > 0:
              player.armor = self.armor
          if self.mana > 0:
              player.mana += spell.mana
          self.timer -= 1

  def cancel_effect(self, player, boss):
      if self.armor > 0 and self.timer <= 0:
          player.armor = 0

SPELLS = [Spell('Magic Missle', 53, 0, 4, 0, 0, 0),
          Spell('Drain', 73, 0, 2, 2, 0, 0),
          Spell('Shield', 113, 6, 0, 0, 7, 0),
          Spell('Poison', 173, 6, 3, 0, 0, 0),
          Spell('Recharge', 229, 5, 0, 0, 0, 101)]

if __name__ == "__main__":
    player = Wizard(50, 500)
    boss = Boss(55, 8)