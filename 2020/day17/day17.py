#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._parse_data()

    def _parse_data(self):
        self._grid = [[[1 if ch == '#' else 0 for ch in line] for line in self._raw_data]]

    def _new_grid(self):
        nplanes = len(self._grid) + 2
        nrows = len(self._grid[0]) + 2
        ncols = len(self._grid[0][0]) + 2
        return [[[0] * ncols for y in range(0, nrows)] for z in range(0, nplanes)]

    def _is_active(self, x, y, z):
        x -= 1
        y -= 1
        z -= 1
        if z < 0 or y < 0 or x < 0:
            return False
        if z > len(self._grid) - 1 or y > len(self._grid[0]) - 1 or x > len(self._grid[0][0]) - 1:
            return False
        return self._grid[z][y][x] == 1

    def _count_active_neighbors(self, x0, y0, z0):
        result = 0
        for z in range(z0 - 1, z0 + 2):
            for y in range(y0 - 1, y0 + 2):
                for x in range(x0 - 1, x0 + 2):
                    if (x, y, z) == (x0, y0, z0):
                        continue
                    if self._is_active(x, y, z):
                        result += 1
        return result

    def _do_cycle(self, method=1):
        new_grid = self._new_grid()
        for z in range(0, len(new_grid)):
            for y in range(0, len(new_grid[0])):
                for x in range(0, len(new_grid[0][0])):
                    n = self._count_active_neighbors(x, y, z)
                    value = 0
                    if self._is_active(x, y, z):
                        if n == 2 or n == 3:
                            value = 1
                    else:
                        if n == 3:
                            value = 1
                    new_grid[z][y][x] = value
        self._grid = new_grid

    def _count_active(self):
        result = 0
        for plane in self._grid:
            for row in plane:
                result += sum(row)
        return result

    def do_part1(self):
        for i in range(0, 6):
            self._do_cycle()
        return self._count_active()

    def do_part2(self):
        self._parse_data()
        for i in range(0, 6):
            self._do_cycle(2)
        return self._count_active()

    def execute(self):
        print('Part 1 result:', self.do_part1())
        #print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
