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


def play_game(player, boss):
    def apply_effects():
        nonlocal player, boss, timers
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
        nonlocal player, boss, timers
        spell = SPELLS[key]
        player.mana -= spell.cost
        if spell.duration > 0:
            timers[key] = spell.duration
        else:
            boss.hit_points -= spell.damage
            player.hit_points += spell.healing

    def play_round(spent=0):
        nonlocal player, boss, timers, winning_costs
        apply_effects()
        if boss.hit_points <= 0:
            winning_costs.append(spent)
            return
        saved_player = player.copy()
        saved_boss = boss.copy()
        saved_timers = timers.copy()
        for key in saved_player.can_cast_spells(timers):
            player = saved_player.copy()
            boss =  saved_boss.copy()
            timers = saved_timers.copy()
            cast_spell(key)
            spell = SPELLS[key]
            if boss.hit_points <= 0:
                winning_costs.append(spent + spell.cost)
                continue
            apply_effects()
            if boss.hit_points <= 0:
                winning_costs.append(spent + spell.cost)
                continue
            player.hit_points -= max(1, boss.damage - player.armor)
            if player.hit_points <= 0:
                continue
            play_round(spent + spell.cost)

    timers = {}
    winning_costs = []
    play_round()
    if len(winning_costs) > 0:
        return True, min(winning_costs)
    return False, 0


if __name__ == "__main__":
    player_won, cost = play_game(Player(50, 500), Boss(55, 8))
    print('Part One: Player {0}, cost {1}'.format('won' if player_won else 'lost', cost))
