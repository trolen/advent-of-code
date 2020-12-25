#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._grid = [[0]]
        self._ref_x = 0
        self._ref_y = 0

    def _parse_directions(self, line):
        result = []
        i = 0
        while i < len(line):
            if line[i] in 'ns':
                result.append(line[i:i+2])
                i += 1
            else:
                result.append(line[i])
            i += 1
        return result

    def _move(self, direction):
        if direction in ['e', 'ne']:
            self._y -= 1
        if direction in ['sw', 'w']:
            self._y += 1
        if direction in ['e', 'se']:
            self._x += 1
        if direction in ['w', 'nw']:
            self._x -= 1

    def _insert_columns(self, n):
        for i in range(0, len(self._grid)):
            for j in range(0, n):
                self._grid[i].insert(0, 0)

    def _append_columns(self, n):
        for i in range(0, len(self._grid)):
            for j in range(0, n):
                self._grid[i].append(0)

    def _insert_rows(self, n):
        for i in range(0, n):
            row = [0] * len(self._grid[0])
            self._grid.insert(0, row)

    def _append_rows(self, n):
        for i in range(0, n):
            row = [0] * len(self._grid[0])
            self._grid.append(row)

    def _adjust_grid(self):
        lrow0 = len(self._grid[0])
        if self._x < 0:
            n = abs(self._x)
            self._insert_columns(n)
            self._ref_x += n
            self._x = 0
        elif self._x >= lrow0:
            n = self._x - lrow0 + 1
            self._append_columns(n)
        lgrid = len(self._grid)
        if self._y < 0:
            n = abs(self._y)
            self._insert_rows(n)
            self._ref_y += n
            self._y = 0
        elif self._y >= lgrid:
            n = self._y - lgrid + 1
            self._append_rows(n)

    def _flip_current_tile(self):
        n = self._grid[self._y][self._x]
        self._grid[self._y][self._x] = 1 - n

    def do_part1(self):
        for line in self._raw_data:
            self._x = self._ref_x
            self._y = self._ref_y
            directions = self._parse_directions(line)
            for direction in directions:
                self._move(direction)
            self._adjust_grid()
            self._flip_current_tile()
        return sum([sum(row) for row in self._grid])

    def _sum_adjacent(self, x, y):
        (ne, e, se, sw, w, nw) = (0, 0, 0, 0, 0, 0)
        l = len(self._grid)
        l0 = len(self._grid[0])
        if y > 0:
            ne = self._grid[y-1][x]
        if y > 0 and x < l0 - 1:
            e = self._grid[y-1][x+1]
        if x < l0 - 1:
            se = self._grid[y][x+1]
        if y < l - 1:
            sw = self._grid[y+1][x]
        if y < l - 1 and x > 0:
            w = self._grid[y+1][x-1]
        if x > 0:
            nw = self._grid[y][x-1]
        return sum([ne, e, se, sw, w, nw])

    def _do_one_day(self):
        self._insert_columns(1)
        self._append_columns(1)
        self._insert_rows(1)
        self._append_rows(1)
        new_grid = []
        for y in range(0, len(self._grid)):
            new_grid.append(self._grid[y][:])
            for x in range(0, len(self._grid[y])):
                n = self._sum_adjacent(x, y)
                if self._grid[y][x] == 1 and (n == 0 or n > 2):
                    new_grid[y][x] = 0
                if self._grid[y][x] == 0 and n == 2:
                    new_grid[y][x] = 1
        self._grid = new_grid

    def do_part2(self):
        for i in range(0, 100):
            self._do_one_day()
        return sum([sum(row) for row in self._grid])

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
