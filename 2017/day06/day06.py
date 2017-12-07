#! /usr/bin/env python3

class Debugger:
    def __init__(self, data):
        self._data = data
        self.reset()

    def reset(self):
        self._blocks = [int(bank) for bank in self._data.split()]
        self._states = []

    def _get_state(self):
        return ''.join([str(block) for block in self._blocks])

    def _redistribute(self):
        maxBlock = max(self._blocks)
        idxMax = self._blocks.index(maxBlock)
        value = self._blocks[idxMax]
        self._blocks[idxMax] = 0
        idx = idxMax + 1
        while value > 0:
            self._blocks[idx % len(self._blocks)] += 1
            idx += 1
            value -= 1

    def reallocate_blocks(self):
        self._states.append(self._get_state())
        found = False
        while not found:
            self._redistribute()
            state = self._get_state()
            if state in self._states:
                found = True
            self._states.append(state)
        return len(self._states) - 1

    def get_loop_size(self):
        idx = self._states.index(self._states[-1])
        return len(self._states) - idx - 1


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


if __name__ == '__main__':
    data = read_data('input.txt')
    debugger = Debugger(data)
    print('Part One: {0}'.format(debugger.reallocate_blocks()))
    print('Part Two: {0}'.format(debugger.get_loop_size()))
