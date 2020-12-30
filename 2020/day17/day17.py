#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._method = 1
        self._raw_data = raw_data
        self._parse_data()

    def _activate_cell(self, x0, y0, z0, w0):
        if (x0, y0, z0, w0) in self._active_cells:
            return
        self._active_cells.add((x0, y0, z0, w0))
        w_start = w0 if self._method == 1 else w0 - 1
        w_end = w0 + 1 if self._method == 1 else w0 + 2
        for w in range(w_start, w_end):
            for z in range(z0 - 1, z0 + 2):
                for y in range(y0 - 1, y0 + 2):
                    for x in range(x0 - 1, x0 + 2):
                        if (x, y, z, w) == (x0, y0, z0, w0):
                            continue
                        n = 0
                        if (x, y, z, w) in self._active_neighbors:
                            n = self._active_neighbors[(x, y, z, w)]
                        self._active_neighbors[(x, y, z, w)] = n + 1

    def _parse_data(self):
        self._active_neighbors = {}
        self._active_cells = set()
        for y in range(0, len(self._raw_data)):
            for x in range(0, len(self._raw_data[y])):
                if self._raw_data[y][x] == '#':
                    self._activate_cell(x, y, 0, 0)

    def _do_cycle(self):
        prev_active_cells = self._active_cells
        prev_active_neighbors = self._active_neighbors
        self._active_cells = set()
        self._active_neighbors = {}
        minX = minY = minZ = minW = 1000000
        maxX = maxY = maxZ = maxW = -1000000
        for (x, y, z, w) in prev_active_cells:
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)
            minZ = min(minZ, z)
            maxZ = max(maxZ, z)
            minW = min(minW, w)
            maxW = max(maxW, w)
        w_start = 0 if self._method == 1 else minW - 1
        w_end = 1 if self._method == 1 else maxW + 2
        for w in range(w_start, w_end):
            for z in range(minZ-1, maxZ+2):
                for y in range(minY-1, maxY+2):
                    for x in range(minX-1, maxX+2):
                        n = 0
                        if (x, y, z, w) in prev_active_neighbors:
                            n = prev_active_neighbors[(x, y, z, w)]
                        if (x, y, z, w) in prev_active_cells:
                            if n == 2 or n == 3:
                                self._activate_cell(x, y, z, w)
                        else:
                            if n == 3:
                                self._activate_cell(x, y, z, w)

    def do_part1(self):
        for i in range(0, 6):
            self._do_cycle()
        return len(self._active_cells)

    def do_part2(self):
        self._method = 2
        self._parse_data()
        for i in range(0, 6):
            self._do_cycle()
        return len(self._active_cells)

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
