#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        line = raw_data[0]
        self._starting_cups = [int(ch) for ch in line]
        self._cups = self._starting_cups[:]
        self._current_cup = 0
        self._min = min(self._cups)
        self._max = max(self._cups)

    def _pick_up(self, num):
        current_value = self._cups[self._current_cup]
        start = self._current_cup + 1
        end = start + num
        l = len(self._cups)
        picked_up = []
        for i in range(start, end):
            picked_up.append(self._cups[i % l])
        for n in picked_up:
            self._cups.remove(n)
        self._current_cup = self._cups.index(current_value)
        return picked_up

    def _normalize_cup_value(self, value):
        if value < self._min:
            return self._max
        if value > self._max:
            return self._min
        return value

    def _find_destination(self):
        dest_value = self._normalize_cup_value(self._cups[self._current_cup] - 1)
        while dest_value not in self._cups:
            dest_value = self._normalize_cup_value(dest_value - 1)
        return self._cups.index(dest_value)

    def _do_move(self):
        picked_up = self._pick_up(3)
        destination = self._find_destination()
        current_value = self._cups[self._current_cup]
        if destination + 1 > len(self._cups) - 1:
            self._cups = self._cups + picked_up
        else:
            n = destination + 1
            self._cups[n:n] = picked_up
        self._current_cup = (self._cups.index(current_value) + 1) % len(self._cups)

    def _do_moves(self, num):
        for i in range(0, num):
            self._do_move()

    def _cups_as_string(self):
        idx = self._cups.index(1)
        l = len(self._cups)
        result = ''
        for i in range(1, l):
            n = (idx + i) % l
            result += str(self._cups[n])
        return result

    def do_part1(self):
        self._do_moves(100)
        return self._cups_as_string()

    def _reset_for_part2(self):
        self._cups = self._starting_cups
        self._current_cup = 0
        for i in range(self._max + 1, 1000000):
            self._cups.append(i)
        self._max = 1000000

    def _get_part2_result(self):
        idx = self._cups.index(1)
        l = len(self._cups)
        result = []
        for i in range(idx + 1, idx + 3):
            n = i % l
            result.append(self._cups[n])
        return result

    def do_part2(self):
        #self._reset_for_part2()
        #self._do_moves(10000000)
        #print(self._get_part2_result())
        return 0

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
