#! /usr/bin/env python3


class HexGrid:
    def __init__(self):
        self.reset()
        self._increments = {
            'ne': (+1, 0),
            'sw': (-1, 0),
            'n': (+1, +1),
            's': (-1, -1),
            'nw': (0, +1),
            'se': (0, -1)
        }

    def reset(self):
        self._x = 0
        self._y = 0
        self._max_steps_from_start = 0
        return self

    def _follow_direction(self, direction):
        self._x += self._increments[direction][0]
        self._y += self._increments[direction][1]
        self._max_steps_from_start = max(self._max_steps_from_start, self.steps_from_start())

    def follow_directions(self, directions):
        for d in directions.split(','):
            self._follow_direction(d)

    def steps_from_start(self):
        return max(abs(self._x), abs(self._y))

    def max_steps_from_start(self):
        return self._max_steps_from_start


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


if __name__ == '__main__':
    data = read_data('input.txt')
    hex_grid = HexGrid()
    hex_grid.follow_directions(data)
    print('Part One: {0}'.format(hex_grid.steps_from_start()))
    print('Part Two: {0}'.format(hex_grid.max_steps_from_start()))
