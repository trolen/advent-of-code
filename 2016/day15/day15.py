#! /usr/bin/env python3


class DiscGame:
    def __init__(self, data):
        self._parse_data(data)

    def _parse_data(self, data):
        self._discs = []
        for line in data:
            terms = line.split()
            positions = int(terms[3])
            s = ''.join(ch if ch.isnumeric() else '' for ch in terms[-1])
            start = int(s)
            self._discs.append((positions, start))

    def _disc_position(self, disc, time):
        positions = self._discs[disc][0]
        start = self._discs[disc][1]
        return (start + time) % positions

    def _push_button(self, time):
        for idx in range(len(self._discs)):
            time += 1
            if self._disc_position(idx, time) != 0:
                return False
        return True

    def get_first_capsule(self):
        time = 0
        while not self._push_button(time):
            time += 1
        return time

    def add_disc(self, positions, start):
        self._discs.append((positions, start))


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    game = DiscGame(data)
    print('Part One: {0}'.format(game.get_first_capsule()))
    game.add_disc(11, 0)
    print('Part Two: {0}'.format(game.get_first_capsule()))
