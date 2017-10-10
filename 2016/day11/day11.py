#! /usr/bin/env python3

class Component:
    def __init__(self, element, type):
        self.element = element
        self.type = type

    def __str__(self):
        return '({0}, {1})'.format(self.element, self.type)


class Simulator:
    def __init__(self, data):
        self._floors = []
        self._parse_data(data)

    def _parse_data(self, data):
        for line in data:
            self._floors.append(self._parse_line(line))

    def _parse_line(self, line):
        result = []
        prev_word = ''
        for word in line.split():
            if word == 'nothing':
                return []
            if word.startswith('gen') or word.startswith('mic'):
                result.append(Component(prev_word[:2], word[:3]))
            prev_word = word
        return result


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    simulator = Simulator(data)
