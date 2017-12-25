#! /usr/bin/env python3

from collections import deque

class Program:
    def __init__(self, prog_id, instructions):
        self._instructions = instructions
        self._pos = 0
        self._registers = {}
        self._buffer_out = deque()
        self._buffer_in = deque()
        self._registers['p'] = prog_id

    def _get_reg(self, reg):
        if not reg in self._registers:
            self._registers[reg] = 0
        return self._registers[reg]

    def _get_reg_or_val(self, arg):
        try:
            result = int(arg)
        except:
            result = self._get_reg(arg)
        return result

    def _snd(self, arg):
        self._buffer_out.append(self._get_reg_or_val(arg))

    def _set(self, reg, arg):
        val = self._get_reg_or_val(arg)
        self._registers[reg] = val

    def _add(self, reg, arg):
        val = self._get_reg_or_val(arg)
        self._registers[reg] = self._get_reg(reg) + val

    def _mul(self, reg, arg):
        val = self._get_reg_or_val(arg)
        self._registers[reg] = self._get_reg(reg) * val

    def _mod(self, reg, arg):
        val = self._get_reg_or_val(arg)
        self._registers[reg] = self._get_reg(reg) % val

    def _rcv(self, reg):
        if len(self._buffer_in) > 0:
            self._registers[reg] = self._buffer_in.popleft()
            return True
        return False

    def _jgz(self, arg1, arg2):
        if self._get_reg_or_val(arg1) > 0:
            return self._get_reg_or_val(arg2)
        return 1

    def run(self):
        while 0 <= self._pos and self._pos < len(self._instructions):
            terms = self._instructions[self._pos].split()
            cmd = terms[0]
            if cmd == 'snd':
                self._snd(terms[1])
            elif cmd == 'set':
                self._set(terms[1], terms[2])
            elif cmd == 'add':
                self._add(terms[1], terms[2])
            elif cmd == 'mul':
                self._mul(terms[1], terms[2])
            elif cmd == 'mod':
                self._mod(terms[1], terms[2])
            elif cmd == 'rcv':
                if not self._rcv(terms[1]):
                    break
            elif cmd == 'jgz':
                self._pos += self._jgz(terms[1], terms[2])
                continue
            self._pos += 1

    def get_output(self):
        buffer = self._buffer_out
        self._buffer_out = deque()
        return buffer

    def set_input(self, buffer):
        self._buffer_in = buffer


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


def solo(data):
    prog = Program(0, data)
    prog.run()
    buffer = prog.get_output()
    return buffer.pop()


def duet(data):
    prog0 = Program(0, data)
    prog1 = Program(1, data)
    buffer = deque()
    result = 0
    while True:
        prog0.set_input(buffer)
        prog0.run()
        buffer = prog0.get_output()
        prog1.set_input(buffer)
        prog1.run()
        buffer = prog1.get_output()
        n = len(buffer)
        result += n
        if n == 0:
            break
    return result


if __name__ == '__main__':
    data = read_data('input.txt')
    print('Part One: {0}'.format(solo(data)))
    print('Part Two: {0}'.format(duet(data)))
