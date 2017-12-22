#! /usr/bin/env python3

class Layer:
    def __init__(self, range):
        self._range = range

    def position(self, tick=0):
        divisor = self._range - 1
        pos = tick % divisor
        dir = tick // divisor
        return self._range - pos if (dir % 2) else pos

    def range(self):
        return self._range


class Firewall:
    def __init__(self, data):
        self._layers = {}
        self._parse_data(data)

    def _parse_data(self, data):
        for line in data:
            layer, range = (int(t.strip(':')) for t in line.split())
            self._layers[layer] = Layer(range)

    def _run(self, delay=0):
        self._severity = 0
        caught = False
        for key in range(max(self._layers.keys()) + 1):
            if key in self._layers:
                layer = self._layers[key]
                if layer.position(delay + key) == 0:
                    self._severity += key * layer.range()
                    caught = True
                    if delay > 0:
                        break
        return caught

    def find_severity(self):
        self._run()
        return self._severity

    def find_min_delay(self):
        delay = 0
        while self._run(delay):
            print('\r{0}'.format(delay), end='')
            delay += 1
        print('\r{0}'.format(delay))
        return delay


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    firewall = Firewall(data)
    print('Part One: {0}'.format(firewall.find_severity()))
    print('Part Two: {0}'.format(firewall.find_min_delay()))
