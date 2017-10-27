#! /usr/bin/env python3

class Computer:
    def __init__(self):
        self.clear_registers()

    def clear_registers(self):
        self._registers = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0
        }

    def get_register(self, register):
        if register in self._registers:
            return self._registers[register]
        return None

    def set_register(self, register, value):
        if register in self._registers:
            self._registers[register] = value

    def _get_register_or_value(self, term):
        if term in self._registers:
            return self._registers[term]
        return int(term)

    def process_instructions(self, lines):
        idx = 0
        while 0 <= idx < len(lines):
            terms = lines[idx].split()
            if terms[0] == 'cpy':
                self._registers[terms[2]] = self._get_register_or_value(terms[1])
            elif terms[0] == 'inc':
                self._registers[terms[1]] += 1
            elif terms[0] == 'dec':
                self._registers[terms[1]] -= 1
            elif terms[0] == 'jnz':
                value = self._get_register_or_value(terms[1])
                if value != 0:
                    idx += int(terms[2])
                    continue
            idx += 1


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    computer = Computer()
    computer.process_instructions(data)
    print('Part One: {0}'.format(computer.get_register('a')))
    computer.clear_registers()
    computer.set_register('c', 1)
    computer.process_instructions(data)
    print('Part Two: {0}'.format(computer.get_register('a')))
