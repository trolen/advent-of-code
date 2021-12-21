#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        self._asteroids = []
        for r in range(0, len(raw_data)):
            row = raw_data[r]
            for c in range(0, len(row)):
                if row[c] == '#':
                    self._asteroids.append((r, c))

    def do_part1(self):
        return (len(self._asteroids), self._asteroids)

    def do_part2(self):
        pass

    def execute(self):
        print('Part 1:', self.do_part1())
        #print('Part 2:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
