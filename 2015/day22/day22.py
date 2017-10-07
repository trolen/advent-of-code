#!/usr/bin/env python3


class Spell:
    def __init__(self, cost, duration, damage, healing, armor, mana):
        self.cost = cost
        self.duration = duration
        self.damage = damage
        self.healing = healing
        self.armor = armor
        self.mana = mana


SPELLS = {
    'Magic Missle': Spell(53, 0, 4, 0, 0, 0),
    'Drain': Spell(73, 0, 2, 2, 0, 0),
    'Shield': Spell(113, 6, 0, 0, 7, 0),
    'Poison': Spell(173, 6, 3, 0, 0, 0),
    'Recharge': Spell(229, 5, 0, 0, 0, 101)
}


class Player:
    def __init__(self, hit_points, mana, armor=0):
        self.hit_points = hit_points
        self.mana = mana
        self.armor = armor

    def copy(self):
        return Player(self.hit_points, self.mana, self.armor)

    def can_cast_spells(self, timers):
        for key in SPELLS:
            spell = SPELLS[key]
            if self.mana < spell.cost:
                continue
            if key in timers:
                continue
            yield key


class Boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    def copy(self):
        return Boss(self.hit_points, self.damage)


def play_game(player, boss, timers={}):
    def apply_effects():
        keys = [timer for timer in timers]
        for key in keys:
            spell = SPELLS[key]
            boss.hit_points -= spell.damage
            if spell.armor > 0:
                player.armor = spell.armor
            player.mana += spell.mana
            timers[key] -= 1
            if timers[key] == 0:
                if spell.armor > 0:
                    player.armor = 0
                del timers[key]

    def cast_spell(key):
        spell = SPELLS[key]
        player.mana -= spell.cost
        if spell.duration > 0:
            timers[key] = spell.duration
        else:
            boss.hit_points -= spell.damage
            player.hit_points += spell.healing

    apply_effects()
    if boss.hit_points <= 0:
        return True, 0
    saved_player = player.copy()
    saved_boss = boss.copy()
    saved_timers = timers.copy()
    for key in saved_player.can_cast_spells(timers):
        spell = SPELLS[key]
        player = saved_player.copy()
        boss =  saved_boss.copy()
        timers = saved_timers.copy()
        cast_spell(key)
        if boss.hit_points <= 0:
            return True, spell.cost
        apply_effects()
        if boss.hit_points <= 0:
            return True, spell.cost
        player.hit_points -= max(1, boss.damage - player.armor)
        if player.hit_points <= 0:
            continue
        player_won, cost = play_game(player, boss, timers)
        if player_won:
            return True, cost + spell.cost
    return False, 0


if __name__ == "__main__":
    player_won, cost = play_game(Player(50, 500), Boss(55, 8))
    print('Part One: Player {0}, cost {1}'.format('won' if player_won else 'lost', cost))
