#! /usr/bin/env python3

class KnotHash:
    def __init__(self, num_elements):
        self._num_elements = num_elements
        self.reset()

    def reset(self):
        self._elements = [_ for _ in range(self._num_elements)]
        self._pos = 0
        self._skip = 0

    def _reverse_sublist(self, n):
        new_list = self._elements + self._elements
        sublist = new_list[self._pos : self._pos+n]
        sublist.reverse()
        for c in sublist:
            self._elements[self._pos] = c
            self._pos = (self._pos + 1) % self._num_elements
        self._pos = (self._pos + self._skip) % self._num_elements
        self._skip += 1

    def hash_one(self, data):
        for n in data.split(','):
            self._reverse_sublist(int(n))
        return self._elements[0] * self._elements[1]

    def hash_64(self, data):
        lengths = [ord(ch) for ch in data]
        lengths += [17, 31, 73, 47, 23]
        for _ in range(64):
            for n in lengths:
                self._reverse_sublist(n)
        hash = ''
        for i in range(16):
            result = 0
            for j in range(16):
                result ^= self._elements[i * 16 + j]
            hash += '{:02x}'.format(result)
        return hash


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


if __name__ == '__main__':
    data = read_data('input.txt')
    knot_hash = KnotHash(256)
    print('Part One: {0}'.format(knot_hash.hash_one(data)))
    knot_hash.reset()
    print('Part Two: {0}'.format(knot_hash.hash_64(data)))
