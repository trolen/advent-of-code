#! /usr/bin/env python3

class Maze:
    def __init__(self, data):
        self._data = data
        self.reset()

    def reset(self):
        self._maze = [int(value) for value in self._data]

    def _jump(self, pos, part2):
        result = pos + self._maze[pos]
        self._maze[pos] += 1 if not part2 or self._maze[pos] < 3 else -1
        return result

    def escape(self, part2=False):
        pos = 0
        steps = 0
        while pos < len(self._maze):
            pos = self._jump(pos, part2)
            steps += 1
        return steps


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    maze = Maze(data)
    print('Part One: {0}'.format(maze.escape()))
    maze.reset()
    print('Part Two: {0}'.format(maze.escape(part2=True)))
