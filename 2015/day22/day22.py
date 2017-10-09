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

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.hit_points, self.mana, self.armor)

    def __repr__(self):
        return 'Player(hit_points={0}, mana={1}, armor={2})'.format(self.hit_points, self.mana, self.armor)

    def iterate_spells(self, active_spells):
        for key in SPELLS:
            spell = SPELLS[key]
            if key in active_spells:
                continue
            if self.mana < spell.cost:
                continue
            yield key


class Boss:
    def __init__(self, hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    def copy(self):
        return Boss(self.hit_points, self.damage)

    def __str__(self):
        return '({0}, {1})'.format(self.hit_points, self.damage)

    def __repr__(self):
        return 'Boss(hit_points={0}, damage={1})'.format(self.hit_points, self.damage)


class Simulator:
    def __init__(self, player, boss, difficulty=0):
        self._player = player
        self._boss = boss
        self._active_spells = {}
        self._min_spent = None
        self._difficulty = difficulty

    def _apply_active_spells(self):
        keys = [key for key in self._active_spells]
        for key in keys:
            spell = SPELLS[key]
            self._boss.hit_points -= spell.damage
            if spell.armor > 0:
                self._player.armor = spell.armor
            self._player.mana += spell.mana
            self._active_spells[key] -= 1
            if self._active_spells[key] == 0:
                if spell.armor > 0:
                    self._player.armor = 0
                del self._active_spells[key]

    def _cast_spell(self, key):
        spell = SPELLS[key]
        self._player.mana -= spell.cost
        if spell.duration > 0:
            self._active_spells[key] = spell.duration
        else:
            self._boss.hit_points -= spell.damage
            self._player.hit_points += spell.healing

    def _set_min_spent(self, value):
        if self._min_spent is None or value < self._min_spent:
            self._min_spent = value

    def _play_round(self, spent=0):
        if self._difficulty > 0:
            self._player.hit_points -= 1
            if self._player.hit_points <= 0:
                return
        self._apply_active_spells()
        if self._boss.hit_points <= 0:
            self._set_min_spent(spent)
            return
        saved_player = self._player.copy()
        saved_boss = self._boss.copy()
        saved_active_spells = self._active_spells.copy()
        for key in saved_player.iterate_spells(self._active_spells):
            self._player = saved_player.copy()
            self._boss =  saved_boss.copy()
            self._active_spells = saved_active_spells.copy()
            self._cast_spell(key)
            spell = SPELLS[key]
            if self._min_spent is not None and (spent + spell.cost) > self._min_spent:
                continue
            if self._boss.hit_points <= 0:
                self._set_min_spent(spent + spell.cost)
                continue
            self._apply_active_spells()
            if self._boss.hit_points <= 0:
                self._set_min_spent(spent + spell.cost)
                continue
            self._player.hit_points -= max(1, self._boss.damage - self._player.armor)
            if self._player.hit_points <= 0:
                continue
            self._play_round(spent + spell.cost)

    def run(self):
        self._play_round()
        return self._min_spent


if __name__ == "__main__":
    simulator = Simulator(Player(50, 500), Boss(55, 8))
    spent = simulator.run()
    print('Part One: Player {0}, cost {1}'.format('won' if spent is not None else 'lost', spent))
    simulator = Simulator(Player(50, 500), Boss(55, 8), 1)
    spent = simulator.run()
    print('Part Two: Player {0}, cost {1}'.format('won' if spent is not None else 'lost', spent))
