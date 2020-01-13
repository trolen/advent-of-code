#! /usr/bin/env python3

import math

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


class Grid:
    def __init__(self, raw_data):
        self._grid = raw_data
        self._num_rows = len(self._grid)
        self._num_cols = len(self._grid[0])

    def _find_next_asteroid(self):
        for r in range(0, self._num_rows):
            for c in range(0, self._num_cols):
                if self._grid[r][c] == '#':
                    yield r, c

    def _detect_asteroids(self, r0, c0):
        result = 0
        for r, c in self._find_next_asteroid():
            if r == r0 and c == c0:
                continue
            d1 = r - r0
            d2 = c - c0
            gcd = math.gcd(abs(d1), abs(d2))
            if r == r0:
                if abs(d2) > 1:
                    start = min(c, c0) + 1
                    stop = max(c, c0)
                    found = False
                    for idx in range(start, stop):
                        if self._grid[r][idx] == '#':
                            found = True
                    if found:
                        continue
            elif c == c0:
                if abs(d1) > 1:
                    start = min(r, r0) + 1
                    stop = max(r, r0)
                    found = False
                    for idx in range(start, stop):
                        if self._grid[idx][c] == '#':
                            found = True
                    if found:
                        continue
            elif gcd > 1:
                step1 = d1 // gcd
                step2 = d2 // gcd
                idx1 = r0 + step1
                idx2 = c0 + step2
                found = False
                while idx1 != r:
                    if self._grid[idx1][idx2] == '#':
                        found = True
                    idx1 += step1
                    idx2 += step2
                if found:
                    continue
            result += 1
        return result

    def find_best_station(self):
        found_row = 0
        found_col = 0
        detected_asteroids = 0
        for r, c in self._find_next_asteroid():
            n = self._detect_asteroids(r, c)
            if n > detected_asteroids:
                found_row, found_col = r, c
                detected_asteroids = n
        return found_row, found_col, detected_asteroids


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    grid = Grid(raw_data)
    print(grid.find_best_station())
