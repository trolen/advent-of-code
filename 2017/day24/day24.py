#! /usr/bin/env python3

class Moat:
    def __init__(self, data):
        self._data = data
        self._parse_data()

    def _parse_data(self):
        self._components = []
        for line in self._data:
            endL, endR = (int(x) for x in line.split('/'))
            self._components.append({'left': endL, 'right': endR, 'strength': endL+endR})

    def _reset(self):
        self._max_strength = 0
        self._max_length = 0

    def _build_bridge(self, pins, used, strength, length, part2=False):
        for idx, comp in enumerate(self._components):
            if idx in used:
                continue
            next_pins = -1
            if pins == comp['left']:
                next_pins = comp['right']
            elif pins == comp['right']:
                next_pins = comp['left']
            if next_pins < 0:
                continue
            used_copy = used[:]
            used_copy.append(idx)
            next_strength = strength + comp['strength']
            next_length = length + 1
            if part2:
                if next_length > self._max_length:
                    self._max_length, self._max_strength = (next_length, next_strength)
                elif next_length == self._max_length:
                    self._max_strength = max(self._max_strength, next_strength)
            else:
                self._max_strength = max(self._max_strength, next_strength)
            self._build_bridge(next_pins, used_copy, next_strength, next_length, part2)

    def find_strongest(self):
        self._reset()
        self._build_bridge(0, [], 0, 0)
        return self._max_strength

    def find_longest(self):
        self._reset()
        self._build_bridge(0, [], 0, 0, part2=True)
        return self._max_strength


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    moat = Moat(data)
    print('Part One: {0}'.format(moat.find_strongest()))
    print('Part Two: {0}'.format(moat.find_longest()))
