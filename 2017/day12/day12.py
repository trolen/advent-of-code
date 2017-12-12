#! /usr/bin/env python3

class Pipes:
    def __init__(self, data):
        self._data = data
        self._build_tree(data)

    def _build_tree(self, data):
        self._tree = {}
        for line in data:
            self._parse_line(line)

    def _parse_line(self, line):
        terms = [t.strip(',') for t in line.split()]
        self._tree[terms[0]] = terms[2:]

    def traverse_pipes(self, start):
        open_pipes = [start]
        visited_pipes = []
        for pipe in open_pipes:
            if pipe in visited_pipes:
                continue
            visited_pipes.append(pipe)
            for p in self._tree[pipe]:
                open_pipes.append(p)
        return visited_pipes

    def count_groups(self):
        visited_pipes = self.traverse_pipes('0')
        num_groups = 1
        for p1 in self._tree:
            if p1 in visited_pipes:
                continue
            for p2 in self.traverse_pipes(p1):
                visited_pipes.append(p2)
            num_groups += 1
        return num_groups


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    pipes = Pipes(data)
    print('Part One: {0}'.format(len(pipes.traverse_pipes('0'))))
    print('Part Two: {0}'.format(pipes.count_groups()))
