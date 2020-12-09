#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_data(raw_data):
    result = []
    addr = 0
    for line in raw_data:
        items = line.split()
        result.append((addr, items[0], int(items[1]), 0))
        addr += 1
    return result

def run_program(instructions):
    acc = 0
    pos = 0
    cnt = 0
    while True:
        if pos >= len(instructions):
            print('End of program')
            break
        cnt += 1
        (addr, instr, arg, ord) = instructions[pos]
        if ord > 0:
            print('Infinite loop')
            break
        instructions[pos] = (addr, instr, arg, cnt)
        if instr == 'nop':
            pos += 1
        if instr == 'acc':
            acc += arg
            pos += 1
        if instr == 'jmp':
            pos += arg
    return acc

def reset_program(instructions):
    for i in range(0, len(instructions)):
        (addr, instr, arg, ord) = instructions[i]
        instructions[i] = (addr, instr, arg, 0)

def get_ord(instr):
    return instr[3]

def dump_instructions(instructions):
    instructions = sorted(instructions, key=get_ord)
    for i in range(0, len(instructions)):
        (addr, instr, arg, ord) = instructions[i]
        if ord > 0:
            print(addr, '-', instr, ' ', arg, ' ', ord)

def execute():
    raw_data = read_data('input.txt')
    instructions = parse_data(raw_data)
    print('Part 1 result:', run_program(instructions))
    reset_program(instructions)
    instructions[298] = (298, 'nop', 0, 0)
    print('Part 2 result:', run_program(instructions))
    #print(dump_instructions(instructions))

if __name__ == '__main__':
    execute()
