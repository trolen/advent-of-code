#! /usr/bin/env python3

from collections import deque

class Cluster:
    def __init__(self, data):
        self._directions = {'u':(-1,0), 'd':(+1,0), 'l':(0,-1), 'r':(0,+1)}
        self._right_turns = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
        self._left_turns = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}
        self._reverse_turns = {'u': 'd', 'd': 'u', 'l': 'r', 'r': 'l'}
        self._data = data

    def _reset(self):
        self._grid = deque()
        for line in self._data:
            self._grid.append(deque(line))
        self._row = len(self._grid) // 2
        self._col = len(self._grid[0]) // 2
        self._dir = 'u'

    def _insert_row(self):
        row = deque(['.' for _ in range(len(self._grid[0]))])
        self._grid.insert(0, row)
        self._row += 1

    def _append_row(self):
        row = deque(['.' for _ in range(len(self._grid[0]))])
        self._grid.append(row)

    def _insert_col(self):
        for row in self._grid:
            row.insert(0, '.')
        self._col += 1

    def _append_col(self):
        for row in self._grid:
            row.append('.')

    def _turn1(self):
        if self._grid[self._row][self._col] == '#':
            self._dir = self._right_turns[self._dir]
        else:
            self._dir = self._left_turns[self._dir]

    def _turn2(self):
        ch = self._grid[self._row][self._col]
        if ch == '.':
            self._dir = self._left_turns[self._dir]
        elif ch == '#':
            self._dir = self._right_turns[self._dir]
        elif ch == 'F':
            self._dir = self._reverse_turns[self._dir]

    def _action1(self):
        result = False
        if self._grid[self._row][self._col] == '.':
            self._grid[self._row][self._col] = '#'
            result = True
        else:
            self._grid[self._row][self._col] = '.'
        return result

    def _action2(self):
        result = False
        ch = self._grid[self._row][self._col]
        if ch == '.':
            ch = 'W'
        elif ch == 'W':
            ch = '#'
            result = True
        elif ch == '#':
            ch = 'F'
        else:
            ch = '.'
        self._grid[self._row][self._col] = ch
        return result

    def _move(self):
        if self._dir == 'u' and self._row == 0:
            self._insert_row()
        elif self._dir == 'd' and self._row == len(self._grid) - 1:
            self._append_row()
        elif self._dir == 'l' and self._col == 0:
            self._insert_col()
        elif self._dir == 'r' and self._col == len(self._grid[0]) - 1:
            self._append_col()
        incr = self._directions[self._dir]
        self._row += incr[0]
        self._col += incr[1]

    def _burst(self, part2):
        if part2:
            self._turn2()
            result = self._action2()
        else:
            self._turn1()
            result = self._action1()
        self._move()
        return result

    def run(self, bursts, part2=False):
        self._reset()
        infections = 0
        for _ in range(bursts):
            if self._burst(part2):
                infections += 1
        return infections

    def show_grid(self):
        print('\n{0}, {1}'.format(self._row, self._col))
        for r in self._grid:
            for c in r:
                print('{0} '.format(c), end='')
            print()


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    cluster = Cluster(data)
    print('Part One: {0}'.format(cluster.run(10000)))
    print('Part Two: {0}'.format(cluster.run(10000000, part2=True)))
