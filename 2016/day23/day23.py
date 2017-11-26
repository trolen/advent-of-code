#! /usr/bin/env python3

class Interpreter:
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

    def _toggle_instruction(self, instruction):
        terms = instruction.split()
        if terms[0] == 'inc':
            terms[0] = 'dec'
        elif terms[0] in ['dec', 'tgl']:
            terms[0] = 'inc'
        elif terms[0] == 'jnz':
            terms[0] = 'cpy'
        elif terms[0] == 'cpy':
            terms[0] = 'jnz'
        return ' '.join(terms)

    def interpret_instructions(self, instructions):
        idx = 0
        while 0 <= idx < len(instructions):
            terms = instructions[idx].split()
            if terms[0] == 'cpy':
                self._registers[terms[2]] = self._get_register_or_value(terms[1])
            elif terms[0] == 'inc':
                self._registers[terms[1]] += 1
            elif terms[0] == 'dec':
                self._registers[terms[1]] -= 1
            elif terms[0] == 'jnz':
                value = self._get_register_or_value(terms[1])
                if value != 0:
                    idx += self._get_register_or_value(terms[2])
                    continue
            elif terms[0] == 'tgl':
                value = idx + self._get_register_or_value(terms[1])
                if 0 <= value < len(instructions):
                    instructions[value] = self._toggle_instruction(instructions[value])
            idx += 1


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    interpreter = Interpreter()
    interpreter.set_register('a', 7)
    interpreter.interpret_instructions(data)
    print('Part One: {0}'.format(interpreter.get_register('a')))
    data = read_data('input.txt')
    interpreter = Interpreter()
    interpreter.set_register('a', 12)
    interpreter.interpret_instructions(data)
    print('Part Two: {0}'.format(interpreter.get_register('a')))
