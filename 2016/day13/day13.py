#! /usr/bin/env python3

class Grid:
    def __init__(self, fav_number, start_x, start_y):
        self._fav_number = fav_number
        self.reset(start_x, start_y)

    def reset(self, start_x, start_y):
        self._min_steps = 999999
        self._open_nodes = [(start_x, start_y, 0)]
        self._closed_nodes = {}

    def _is_closed(self, x, y):
        return (x,y) in self._closed_nodes

    def _is_open_space(self, x, y):
        result = self._fav_number + x*x + 3*x + 2*x*y + y + y*y
        return (bin(result).count('1') % 2) == 0

    def _check_node(self, node, is_part1=True):
        x = node[0]
        y = node[1]
        steps = node[2]
        if x < 0 or y < 0:
            return False
        if not self._is_open_space(x, y):
            return False
        if self._is_closed(x, y):
            return False
        if is_part1 and x == self._end_x and y == self._end_y:
            if steps < self._min_steps:
                self._min_steps = steps
            return False
        return True

    def _do_pass(self, is_part1=True):
        new_nodes = []
        for node in self._open_nodes:
            x = node[0]
            y = node[1]
            steps = node[2]
            self._closed_nodes[(x,y)] = steps
            steps += 1
            if is_part1:
                if steps >= self._min_steps:
                    continue
            else:
                if steps > self._max_steps:
                    continue
            candidates = [(x - 1, y, steps), (x + 1, y, steps), (x, y - 1, steps), (x, y + 1, steps)]
            for new_node in candidates:
                if self._check_node(new_node, is_part1):
                    new_nodes.append(new_node)
        self._open_nodes = new_nodes

    def find_shortest_path(self, end_x, end_y):
        self._end_x = end_x
        self._end_y = end_y
        while len(self._open_nodes) > 0:
            self._do_pass()
        return self._min_steps

    def count_closed_nodes(self, max_steps):
        self._max_steps = max_steps
        while len(self._open_nodes) > 0:
            self._do_pass(is_part1=False)
        return len(self._closed_nodes)


if __name__ == '__main__':
    grid = Grid(1364, 1, 1)
    print('Part One: {0}'.format(grid.find_shortest_path(31, 39)))
    grid.reset(1, 1)
    print('Part Two: {0}'.format(grid.count_closed_nodes(50)))
