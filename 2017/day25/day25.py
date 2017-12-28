#! /usr/bin/env python3

from collections import deque

class Tape:
    def __init__(self, data):
        self._data = data
        self._parse_data()

    def _parse_data(self):
        self._states = {}
        for line in self._data:
            terms = line.split()
            if len(terms) == 0:
                continue
            t = terms[0]
            if t == 'Begin':
                self._start = terms[-1][0]
                continue
            if t == 'Perform':
                self._steps = int(terms[-2])
                continue
            if t == 'In':
                current_state = {}
                self._states[terms[-1][0]] = current_state
                continue
            if t == 'If':
                current_value = {}
                current_state[int(terms[-1][0])] = current_value
                continue
            if t == '-':
                cmd = terms[1]
                if cmd == 'Write':
                    current_value['Write'] = int(terms[-1][0])
                elif cmd == 'Move':
                    current_value['Move'] = 1 if terms[-1] == 'right.' else -1
                elif cmd == 'Continue':
                    current_value['Continue'] = terms[-1][0]
                continue

    def _reset(self):
        self._tape = deque([0])
        self._cursor = 0
        self._state = self._start

    def run(self):
        self._reset()
        for i in range(self._steps):
            print('\rProgress: {0:02.2f} %'.format(100 * i / self._steps), end='')
            current_state = self._states[self._state]
            current_val = current_state[self._tape[self._cursor]]
            self._tape[self._cursor] = current_val['Write']
            self._state = current_val['Continue']
            self._cursor += current_val['Move']
            if self._cursor < 0:
                self._cursor = 0
                self._tape.insert(0, 0)
            elif self._cursor == len(self._tape):
                self._tape.append(0)
        print('\rProgress: 100 %')
        return sum(self._tape)


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    tape = Tape(data)
    print('Part One: {0}'.format(tape.run()))
