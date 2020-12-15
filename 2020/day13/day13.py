#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._earliest_departure = int(raw_data[0])
        self._parse_data(raw_data[1])

    def _parse_data(self, line):
        self._buses = {}
        items = line.split(',')
        for i in range(0, len(items)):
            if not items[i] == 'x':
                self._buses[int(items[i])] = i

    def do_part1(self):
        t = self._earliest_departure
        while (True):
            for id in self._buses:
                if (t % id) == 0:
                    return id * (t - self._earliest_departure)
            t += 1

    def do_part2(self):
        product = 1
        for id in self._buses.keys():
            product *= id
        nSum = 0
        for id in self._buses.keys():
            p = int(product / id)
            a = -self._buses[id] % id
            nSum += a * pow(p, -1, id) * p
        return nSum % product

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
