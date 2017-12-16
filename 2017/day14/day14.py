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


class Defragmenter:
    def __init__(self, key):
        self._key = key
        self._build_grid()

    def _build_grid(self):
        self._grid = []
        hash = KnotHash(256)
        for idx in range(128):
            data = '{0}-{1}'.format(self._key, idx)
            s = hash.hash_64(data)
            s_bits = ''.join('{0:04b}'.format(int(ch,16)) for ch in s)
            self._grid.append([ch for ch in s_bits])
            hash.reset()

    def count_bits(self):
        result = 0
        for idx in range(128):
            for s in self._grid[idx]:
                result += s.count('1')
        return result

    def _clear_region(self, r, c):
        self._grid[r][c] = '0'
        if r > 0 and self._grid[r-1][c] == '1':
            self._clear_region(r-1, c)
        if c > 0 and self._grid[r][c-1] == '1':
            self._clear_region(r, c-1)
        if r < 127 and self._grid[r+1][c] == '1':
            self._clear_region(r+1, c)
        if c < 127 and self._grid[r][c+1] == '1':
            self._clear_region(r, c+1)

    def count_regions(self):
        result = 0
        for r in range(128):
            for c in range(128):
                ch = self._grid[r][c]
                if ch == '1':
                    result += 1
                    self._clear_region(r, c)
        return result



if __name__ == '__main__':
    key = 'hxtvlmkl'
    defrag = Defragmenter(key)
    print('Part One: {0}'.format(defrag.count_bits()))
    print('Part Two: {0}'.format(defrag.count_regions()))
