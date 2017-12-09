#! /usr/bin/env python3

class Stream:
    def _reset(self):
        self._score = 0
        self._garbage = 0

    def analyze(self, data):
        self._reset()
        group_level = 0
        in_garbage = False
        in_esc = False
        for ch in data:
            if in_esc:
                in_esc = False
                continue
            if ch == '!':
                in_esc = True
                continue
            if in_garbage:
                if ch == '>':
                    in_garbage = False
                else:
                    self._garbage += 1
                continue
            if ch == '<':
                in_garbage = True
                continue
            if ch == '}':
                self._score += group_level
                group_level -= 1
                continue
            if ch == '{':
                group_level += 1

    def score(self):
        return self._score

    def garbage(self):
        return self._garbage


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


if __name__ == '__main__':
    data = read_data('input.txt')
    stream = Stream()
    stream.analyze(data)
    print('Part One: {0}'.format(stream.score()))
    print('Part Two: {0}'.format(stream.garbage()))
