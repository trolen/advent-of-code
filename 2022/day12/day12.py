import sys


def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class Node:
    def __init__(self, ch):
        self.elevation = ord(ch) - ord('a')
        self.distance = sys.maxsize

    def reset_distance(self):
        self.distance = sys.maxsize


class Application:
    def __init__(self, raw_input):
        self._directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._nodes = []
        self._unvisited = []
        r = 0
        for line in raw_input:
            row = []
            c = 0
            for ch in line:
                if ch == 'S':
                    ch = 'a'
                    self._start = (r, c)
                elif ch == 'E':
                    ch = 'z'
                    self._end = (r, c)
                row.append(Node(ch))
                self._unvisited.append((r, c))
                c += 1
            self._nodes.append(row)
            r += 1

    def _visit_node(self, node):
        try:
            self._unvisited.remove(node)
        except:
            print('Error removing node:', node)
            sys.exit(1)
        (r0, c0) = node
        current = self._nodes[r0][c0]
        for d in self._directions:
            r = r0 + d[0]
            c = c0 + d[1]
            if (r, c) in self._unvisited:
                if self._nodes[r][c].elevation <= current.elevation + 1:
                    self._nodes[r][c].distance = current.distance + 1

    def _find_node(self):
        value = sys.maxsize
        result = None
        for node in self._unvisited:
            (r, c) = node
            d = self._nodes[r][c].distance
            if d < value:
                value = d
                result = (r, c)
        return result

    def do_part1(self, start_node=None):
        node = start_node if start_node is not None else self._start
        (r, c) = node
        self._nodes[r][c].distance = 0
        while True:
            self._visit_node(node)
            node = self._find_node()
            if node is None:
                return sys.maxsize
            if node == self._end:
                break
        (r, c) = self._end
        return self._nodes[r][c].distance

    def _reset_nodes(self):
        self._unvisited = []
        for r in range(len(self._nodes)):
            for c in range(len(self._nodes[0])):
                self._unvisited.append((r, c))
                self._nodes[r][c].reset_distance()

    def do_part2(self):
        distances = []
        for r in range(len(self._nodes)):
            for c in range(len(self._nodes[0])):
                node = (r, c)
                if self._nodes[r][c].elevation == 0:
                    self._reset_nodes()
                    distances.append(self.do_part1(node))
        return min(distances)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
