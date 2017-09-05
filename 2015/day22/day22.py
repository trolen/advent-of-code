#!/usr/bin/env python3

class Player:
    def __init__(self, hit_points, armor, mana, damage):
        self.reset(hit_points, armor, mana, damage)

    def reset(self, hit_points, armor, mana, damage):
        self.hit_points = hit_points
        self.armor = armor
        self.mana = mana
        self.damage = damage


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

    def can_cast(self, wizard):
        if wizard.mana < self.cost:
            return False
        if self.timer > 0:
            return False
        return True

    def cast(self, wizard, boss):
        if not self.can_cast(wizard):
            return
        wizard.mana -= self.cost
        if self.effect > 0:
            self.timer = self.effect
        else:
            if self.damage > 0:
                boss.hit_points -= self.damage
            if self.heal > 0:
                wizard.hit_points += self.heal

    def apply_effect(self, wizard, boss):
        if self.effect > 0 and self.timer > 0:
            if self.damage > 0:
                boss.hit_points -= self.damage
            if self.armor > 0:
                wizard.armor = self.armor
            if self.mana > 0:
                wizard.mana += self.mana
            self.timer -= 1

    def cancel_armor_effect(self, wizard):
        if self.armor > 0 and self.timer <= 0:
            wizard.armor = 0


SPELLS = [Spell('Magic Missle', 53, 0, 4, 0, 0, 0),
          Spell('Drain', 73, 0, 2, 2, 0, 0),
          Spell('Shield', 113, 6, 0, 0, 7, 0),
          Spell('Poison', 173, 6, 3, 0, 0, 0),
          Spell('Recharge', 229, 5, 0, 0, 0, 101)]


def apply_effects(wizard, boss):
    for spell in SPELLS:
        spell.apply_effect(wizard, boss)


def cancel_effects(wizard):
    for spell in SPELLS:
        spell.cancel_armor_effect(wizard)


def wizard_turn(wizard, boss, spell):
    apply_effects(wizard, boss)
    if boss.hit_points <= 0:
        return True
    cancel_effects(wizard)
    if spell.can_cast(wizard):
        spell.cast(wizard, boss)
    return boss.hit_points <= 0


def boss_turn(wizard, boss):
    apply_effects(wizard, boss)
    if boss.hit_points <= 0:
        return False
    wizard.hit_points -= max(1, boss.damage - wizard.armor)
    cancel_effects(wizard)
    return wizard.hit_points <= 0


def play_game(wizard, boss):
    pass


if __name__ == "__main__":
    wizard = Player(50, 0, 500, 0)
    boss = Player(55, 0, 0, 8)