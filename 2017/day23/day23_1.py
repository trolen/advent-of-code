#! /usr/bin/env python3

class Program:
    def __init__(self, data):
        self._data = data

    def _init_registers(self):
        registers = {}
        for ch in 'abcdefgh':
            registers[ch] = 0
        return registers

    def _get_reg_or_val(self, arg):
        if arg in self._registers:
            return self._registers[arg]
        return int(arg)

    def _exec_instruction(self, instruction):
        cmd, arg1, arg2 = instruction.split()
        if cmd == 'set':
            self._registers[arg1] = self._get_reg_or_val(arg2)
        elif cmd == 'sub':
            self._registers[arg1] -= self._get_reg_or_val(arg2)
        elif cmd == 'mul':
            self._registers[arg1] *= self._get_reg_or_val(arg2)
            self._mul_count += 1
        elif cmd == 'jnz':
            if self._get_reg_or_val(arg1) != 0:
                return self._get_reg_or_val(arg2)
        return 1

    def run(self, part2=False):
        self._registers = self._init_registers()
        idx = 0
        n = len(self._data)
        self._mul_count = 0
        while 0 <= idx and idx < n:
            idx += self._exec_instruction(self._data[idx])
        return self._mul_count


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    prog = Program(data)
    print('Part One: {0}'.format(prog.run()))
