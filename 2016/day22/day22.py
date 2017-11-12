#! /usr/bin/env python3

class Cluster:
    def __init__(self, df_input):
        self._grid = self._build_grid(df_input)

    def _build_grid(self, df_input):
        grid = {}
        for line in df_input:
            terms = line.split()
            (node_name, size, used, avail) = terms[:4]
            node_info = node_name.split('-')
            x = int(node_info[1][1:])
            y = int(node_info[2][1:])
            if not y in grid:
                grid[y] = {}
            grid[y][x] = {}
            grid[y][x]['size'] = int(size[:-1])
            grid[y][x]['used'] = int(used[:-1])
            grid[y][x]['avail'] = int(avail[:-1])
        return grid

    def _is_viable(self, x1, y1, x2, y2):
        return self._grid[y1][x1]['used'] <= self._grid[y2][x2]['avail']

    def _count_viable_nodes_for_node(self, x, y):
        count = 0
        if self._grid[y][x]['used'] == 0:
            return 0
        for y1 in self._grid.keys():
            for x1 in self._grid[y1].keys():
                if (x,y) == (x1,y1):
                    continue
                if self._is_viable(x, y, x1, y1):
                    count += 1
        return count

    def count_viable_nodes(self):
        count = 0
        for y in self._grid.keys():
            for x in self._grid[y].keys():
                count += self._count_viable_nodes_for_node(x, y)
        return count


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    cluster = Cluster(data)
    print('Part One: {0}'.format(cluster.count_viable_nodes()))
