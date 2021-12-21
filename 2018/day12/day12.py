#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._parse_data()

    def _set_initial_generation(self):
        self._generation = set()
        (prefix, initial_state) = self._raw_data[0].split(': ')
        for i in range(0, len(initial_state)):
            if initial_state[i] == '#':
                self._generation.add(i)
        self._min = min(self._generation)
        self._max = max(self._generation)

    def _parse_data(self):
        self._set_initial_generation()
        self._rules = []
        for line in self._raw_data[2:]:
            self._rules.append(line.split(' => '))

    def _match_rules(self, idx):
        for (pattern, result) in self._rules:
            if result != '#':
                continue
            matched = True
            for i in range(0, 5):
                n = idx - 2 + i
                if pattern[i] == '.' and n in self._generation:
                    matched = False
                    break
                if pattern[i] == '#' and n not in self._generation:
                    matched = False
                    break
            if matched:
                return True
        return False

    def _new_generation(self):
        new_generation = set()
        start = self._min - 2
        end = self._max + 3
        for n in range(start, end):
            if self._match_rules(n):
                new_generation.add(n)
        self._generation = new_generation
        self._min = min(self._generation)
        self._max = max(self._generation)

    def do_part1(self):
        for i in range(0, 20):
            self._new_generation()
        return sum(self._generation)

    def do_part2(self):
        self._set_initial_generation()
        for i in range(0, 50000000000):
            self._new_generation()
        return sum(self._generation)

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
