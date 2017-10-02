#!/usr/bin/env python3


class Spell:
    def __init__(self, name, cost, duration, damage, healing, armor, mana):
        self.name = name
        self.cost = cost
        self.duration = duration
        self.damage = damage
        self.healing = healing
        self.armor = armor
        self.mana = mana


SPELLS = [
    Spell('Magic Missle', 53, 0, 4, 0, 0, 0),
    Spell('Drain', 73, 0, 2, 2, 0, 0),
    Spell('Shield', 113, 6, 0, 0, 7, 0),
    Spell('Poison', 173, 6, 3, 0, 0, 0),
    Spell('Recharge', 229, 5, 0, 0, 0, 101)
]


class Player:
    def __init__(self, hit_points, mana, armor=0):
        self.hit_points = hit_points
        self.mana = mana
        self.armor = armor

    def copy(self):
        return Player(self.hit_points, self.mana, self.armor)

    def can_cast_spells(self, timers):
        for spell in SPELLS:
            if self.mana < spell.cost:
                continue
            if spell.name in timers:
                continue
            yield spell


class Boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    def copy(self):
        return Boss(self.hit_points, self.damage)


def find_spell(name):
    for spell in SPELLS:
        if spell.name == name:
            return spell
    return None


def play_game(player, boss, timers={}):
    new_player = {}
    new_boss = {}
    new_timers = {}

    def apply_effects():
        keys = [k for k in new_timers.keys()]
        for timer in keys:
            spell = find_spell(timer)
            new_boss.hit_points -= spell.damage
            if spell.armor > 0:
                new_player.armor = spell.armor
            new_player.mana += spell.mana
            new_timers[timer] -= 1
            if new_timers[timer] == 0:
                if spell.armor > 0:
                    new_player.armor = 0
                del new_timers[timer]

    def cast_spell(spell):
        new_player.mana -= spell.cost
        if spell.duration > 0:
            new_timers[spell.name] = spell.duration
        else:
            new_boss.hit_points -= spell.damage
            new_player.hit_points += spell.healing


    def player_wins():
        return new_player.hit_points > 0 and new_boss.hit_points <= 0

    def boss_wins():
        return new_player.hit_points <= 0 and new_boss.hit_points > 0

    player_can_cast_spells = [s for s in player.can_cast_spells(new_timers)]
    for spell in player_can_cast_spells:
        new_player = player.copy()
        new_boss = boss.copy()
        new_timers = timers.copy()
        apply_effects()
        if player_wins():
            return True, 0
        cast_spell(spell)
        if player_wins():
            return True, spell.cost
        apply_effects()
        if player_wins():
            return True, spell.cost
        new_player.hit_points -= max(1, new_boss.damage - new_player.armor)
        if boss_wins():
            continue
        player_won, cost = play_game(new_player, new_boss, new_timers)
        if player_won:
            return player_won, cost + spell.cost
    return False, 0


if __name__ == "__main__":
    player_won, cost = play_game(Player(50, 500), Boss(55, 8))
    print('Part One: Player {0}, cost {1}'.format('won' if player_won else 'lost', cost))
