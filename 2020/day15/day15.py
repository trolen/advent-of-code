#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data

    def _parse_data(self):
        self._index = 0
        self._numbers_spoken = {}
        items = self._raw_data[0].split(',')
        for item in items:
            self._add_number(int(item))

    def _add_number(self, n):
        self._index += 1
        a = []
        if n in self._numbers_spoken:
            a = self._numbers_spoken[n]
        a.append(self._index)
        self._numbers_spoken[n] = a
        self._last_number = n

    def _single_turn(self):
        indexes = self._numbers_spoken[self._last_number]
        new_number = 0
        if len(indexes) > 1:
            new_number = indexes[-1] - indexes[-2]
        self._add_number(new_number)

    def _multiple_turns(self, num_turns):
        while self._index < num_turns:
            self._single_turn()

    def do_part1(self):
        self._parse_data()
        self._multiple_turns(2020)
        return self._last_number

    def do_part2(self):
        self._parse_data()
        self._multiple_turns(30000000)
        return self._last_number

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
