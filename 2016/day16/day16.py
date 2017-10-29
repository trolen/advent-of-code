#! /usr/bin/env python3

class Disk:
    def __init__(self, size, initial_state):
        self._size = size
        self._initial_state = initial_state

    def _dragon_curve(self, data):
        return data + '0' + ''.join('1' if c == '0' else '0' for c in data[-1::-1])

    def _compute_checksum(self, data):
        result = data
        while (len(result) % 2) == 0:
            new_result = ''
            for idx in range(0, len(result), 2):
                pair = result[idx:idx+2]
                new_result += '1' if pair == '00' or pair == '11' else '0'
            result = new_result
        return result

    def fill_disk(self):
        data = self._initial_state
        while len(data) < self._size:
            data = self._dragon_curve(data)
        data = data[:self._size]
        return self._compute_checksum(data)


if __name__ == '__main__':
    state = '10011111011011001'
    disk1 = Disk(272, state)
    print('Part One: {0}'.format(disk1.fill_disk()))
    disk2 = Disk(35651584, state)
    print('Part Two: {0}'.format(disk2.fill_disk()))
