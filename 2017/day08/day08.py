#! /usr/bin/env python3

class Interpreter:
    def __init__(self, data):
        self._instructions = data
        self.reset()

    def reset(self):
        self._registers = {}
        self._max_allocation = 0

    def _get_register(self, reg):
        return self._registers[reg] if reg in self._registers else 0

    def _condition(self, reg, oper, val):
        reg_val = self._get_register(reg)
        if oper == '>':
            return reg_val > val
        if oper == '>=':
            return reg_val >= val
        if oper == '<':
            return reg_val < val
        if oper == '<=':
            return reg_val <= val
        if oper == '==':
            return reg_val == val
        if oper == '!=':
            return reg_val != val
        return False

    def _interpret(self, instruction):
        terms = instruction.split()
        if not self._condition(terms[4], terms[5], int(terms[6])):
            return
        reg = terms[0]
        reg_val = self._get_register(reg)
        val = int(terms[2])
        if terms[1] == 'inc':
            self._registers[reg] = reg_val + val
        else:
            self._registers[reg] = reg_val - val
        self._max_allocation = max(self._max_allocation, self._registers[reg])

    def run(self):
        for instr in self._instructions:
            self._interpret(instr)

    def max_register_value(self):
        return max(self._registers.values())

    def max_allocation(self):
        return self._max_allocation


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    interpreter = Interpreter(data)
    interpreter.run()
    print('Part One: {0}'.format(interpreter.max_register_value()))
    print('Part Two: {0}'.format(interpreter.max_allocation()))
