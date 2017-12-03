#! /usr/bin/env python3

import math

class MemoryGrid:
    def __init__(self, data):
        self._target = data
        self._dimension = self._calc_dimension()
        self._start = self._find_start()
        self._end = self._find_end()
        self._grid = [[0 for _ in range(self._dimension)] for _ in range(self._dimension)]

    def _calc_dimension(self):
        result = int(math.sqrt(self._target))
        n = result * result
        if (result % 2) > 0 and n == self._target:
            return result
        result += 1 if (result % 2) == 0 else 2
        return result

    def _find_start(self):
        n = (self._dimension + 1) // 2
        return (n, n)

    def _find_end(self):
        x = self._dimension
        y = self._dimension
        val = self._dimension * self._dimension
        dir = 0
        increments = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while val > self._target:
            x += increments[dir][0]
            y += increments[dir][1]
            val -= 1
            if dir == 0 and x == 1:
                dir = 1
            elif dir == 1 and y == 1:
                dir = 2
            elif dir == 2 and x == self._dimension:
                dir = 3
        return (x, y)

    def calc_distance(self):
        x1, y1 = self._start
        x2, y2 = self._end
        return abs(x1 - x2) + abs(y1 - y2)

    def _get_cell(self, x, y):
        return self._grid[y - 1][x - 1]

    def _set_cell(self, x, y, val):
        self._grid[y - 1][x - 1] = val

    def _sum_adjacent(self, x, y):
        xStart = x - 1 if x > 1 else x
        xEnd = x + 1 if x < self._dimension else x
        yStart = y - 1 if y > 1 else y
        yEnd = y + 1 if y < self._dimension else y
        result = 0
        for x in range(xStart, xEnd + 1):
            for y in range(yStart, yEnd + 1):
                result += self._get_cell(x, y)
        return result

    def part2(self):
        n = 1
        x = self._start[0]
        y = self._start[1]
        self._set_cell(x, y, n)
        dir = 0
        increments = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        while n <= self._target:
            x += increments[dir][0]
            y += increments[dir][1]
            n = self._sum_adjacent(x, y)
            self._set_cell(x, y, n)
            if dir == 0 and self._get_cell(x, y - 1) == 0:
                dir = 1
            elif dir == 1 and self._get_cell(x - 1, y) == 0:
                dir = 2
            elif dir == 2 and self._get_cell(x, y + 1) == 0:
                dir = 3
            elif dir == 3 and self._get_cell(x + 1, y) == 0:
                dir = 0
        return n


if __name__ == '__main__':
    grid = MemoryGrid(312051)
    print('Part One: {0}'.format(grid.calc_distance()))
    print('Part Two: {0}'.format(grid.part2()))
