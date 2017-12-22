#! /usr/bin/env python3

from collections import deque

class DancingPrograms:
    def __init__(self, num_programs, data):
        self._num_programs = num_programs
        self._parse_instructions(data)
        self._functions = {'s': self._spin, 'x': self._swapN, 'p': self._swapP}

    def _parse_instructions(self, data):
        self._instructions = deque()
        for s in data.split(','):
            cmd = s[0]
            instruction = {'cmd': cmd}
            if cmd == 's':
                a1 = int(s[1:])
                a2 = None
            else:
                a1, a2 = (s[1:].split('/'))
                if cmd == 'x':
                    a1 = int(a1)
                    a2 = int(a2)
            instruction['arg1'] = a1
            instruction['arg2'] = a2
            self._instructions.append(instruction)

    def _reset(self):
        self._programs = deque()
        for idx in range(self._num_programs):
            self._programs.append(chr(ord('a') + idx))
        self._to_str()

    def _to_str(self):
        self._str = ''.join(self._programs)
        return self._str

    def str(self):
        return self._str

    def _spin(self, n, _):
        self._programs.rotate(n)

    def _swapN(self, n1, n2):
        self._programs[n1], self._programs[n2] = self._programs[n2], self._programs[n1]

    def _swapP(self, a1, a2):
        self._swapN(self._programs.index(a1), self._programs.index(a2))

    def _dance_move(self, move):
        cmd = move['cmd']
        self._functions[cmd](move['arg1'], move['arg2'])

    def dance(self, repeat=1):
        self._reset()
        seen = []
        repeated = False
        for i in range(repeat):
            if self._str in seen:
                repeated = True
                break
            seen.append(self._str)
            for move in self._instructions:
                self._dance_move(move)
            self._to_str()
        if repeated:
            return seen[repeat % len(seen)]
        return self._str


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


if __name__ == '__main__':
    data = read_data('input.txt')
    programs = DancingPrograms(16, data)
    print('Part One: {0}'.format(programs.dance()))
    print('Part Two: {0}'.format(programs.dance(1000000000)))
