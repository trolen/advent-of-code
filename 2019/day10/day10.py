#! /usr/bin/env python3

import math

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


class Grid:
    def __init__(self, raw_data):
        self._parse_data(raw_data)
        self._num_rows = len(self._grid)
        self._num_cols = len(self._grid[0])

    def _parse_data(self, raw_data):
        self._grid = []
        for line in raw_data:
            row = []
            for ch in line:
                row.append(0 if ch == '.' else 1)
            self._grid.append(row)

    def _find_next_asteroid(self):
        for y in range(0, self._num_rows):
            for x in range(0, self._num_cols):
                if self._grid[y][x] == 1:
                    yield x, y

    def _detect_asteroids(self, x0, y0):
        result = []
        for x, y in self._find_next_asteroid():
            if y == y0 and x == x0:
                continue
            d1 = y - y0
            d2 = x - x0
            gcd = math.gcd(abs(d1), abs(d2))
            if y == y0:
                if abs(d2) > 1:
                    step = 1 if d2 > 0 else -1
                    found = False
                    for idx in range(x0 + step, x, step):
                        if self._grid[y][idx] == 1:
                            found = True
                    if found:
                        continue
            elif x == x0:
                if abs(d1) > 1:
                    step = 1 if d1 > 0 else -1
                    found = False
                    for idx in range(y0 + step, y, step):
                        if self._grid[idx][x] == 1:
                            found = True
                    if found:
                        continue
            elif gcd > 1:
                step1 = d1 // gcd
                step2 = d2 // gcd
                idx1 = y0 + step1
                idx2 = x0 + step2
                found = False
                while idx1 != y:
                    if self._grid[idx1][idx2] == 1:
                        found = True
                        break
                    idx1 += step1
                    idx2 += step2
                if found:
                    continue
            if x == x0:
                angle = 90 if d1 < 0 else 270
            else:
                angle = math.degrees(math.atan(-1 * d1 / d2))
            angle = 90 - angle
            if angle < 0:
                angle += 360
            result.append((angle,x,y))
        return result

    def find_best_station(self):
        found_x = 0
        found_y = 0
        detected_asteroids = 0
        for x, y in self._find_next_asteroid():
            n = len(self._detect_asteroids(x, y))
            if n > detected_asteroids:
                found_x, found_y = x, y
                detected_asteroids = n
        return found_x, found_y, detected_asteroids

    def vaporize_asteroids(self):
        x0, y0, n_detected = self.find_best_station()
        print('Station at: {0}'.format((x0, y0)))
        result = []
        while n_detected > 0:
            asteroids = self._detect_asteroids(x0, y0)
            n_detected = len(asteroids)
            temp = {}
            for a in asteroids:
                temp[a[0]] = a
            for idx in sorted(temp.keys()):
                result.append(temp[idx])
                x = temp[idx][1]
                y = temp[idx][2]
                self._grid[y][x] = 0
        return result

    def show_grid(self):
        for row in self._grid:
            for col in row:
                print('{0}'.format('.' if col == 0 else '#'), end='')
            print()
        print('Asteroids: {0}'.format(self.total_asteroids()))

    def total_asteroids(self):
        return sum(sum(row) for row in self._grid)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    grid = Grid(raw_data)
    x, y, n = grid.find_best_station()
    print('Monitor Station at: {0}, {1}\nNumber of asteroids detected: {2}'.format(x, y, n))
