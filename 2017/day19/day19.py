#! /usr/bin/env python3

import string

class Diagram:
    def __init__(self, data):
        self._directions = {'d':(+1,0), 'r':(0,+1), 'l':(0,-1), 'u':(-1,0)}
        self._grid = []
        for line in data:
            row = []
            for ch in line:
                row.append(ch)
            self._grid.append(row)

    def _next_ch(self, row, col, dir):
        r = row + self._directions[dir][0]
        c = col + self._directions[dir][1]
        if r < 0 or r >= len(self._grid):
            return None
        if c < 0 or c >= len(self._grid[r]):
            return None
        return self._grid[r][c]

    def _change_dir(self, row, col, dir):
        if dir in ['d','u']:
            next_ch = self._next_ch(row, col, 'l')
            if next_ch and (next_ch == '-' or next_ch in string.ascii_uppercase):
                return 'l'
            else:
                return 'r'
        else:
            next_ch = self._next_ch(row, col, 'u')
            if next_ch and (next_ch == '|' or next_ch in string.ascii_uppercase):
                return 'u'
            else:
                return 'd'

    def run(self):
        r = 0
        c = self._grid[r].index('|')
        dir = 'd'
        self._path = ''
        self._steps = 0
        while True:
            self._steps += 1
            ch = self._grid[r][c]
            if ch in string.ascii_uppercase:
                self._path += ch
            if ch == '+':
                dir = self._change_dir(r, c, dir)
            next_ch = self._next_ch(r, c, dir)
            if not next_ch:
                break
            if next_ch == ' ':
                break
            r += self._directions[dir][0]
            c += self._directions[dir][1]

    def path(self):
        return self._path

    def steps(self):
        return self._steps


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip('\n') for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    diagram = Diagram(data)
    diagram.run()
    print('Part One: {0}'.format(diagram.path()))
    print('Part Two: {0}'.format(diagram.steps()))
