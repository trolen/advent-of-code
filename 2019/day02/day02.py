#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def prepare_data(raw_data, noun=None, verb=None):
    data = [int(x) for x in raw_data.split(',')]
    if noun is not None:
        data[1] = noun
    if verb is not None:
        data[2] = verb
    return data


def run_intcode(raw_data, noun=None, verb=None):
    data = prepare_data(raw_data, noun, verb)
    pos = 0
    while True:
        instr = data[pos]
        if instr == 99:
            return data
        posA = data[pos + 1]
        posB = data[pos + 2]
        posC = data[pos + 3]
        '''
        if data[posA] >= len(data):
            return data
        if data[posB] >= len(data):
            return data
        '''
        if instr == 1:
            result = data[posA] + data[posB]
        elif instr == 2:
            result = data[posA] * data[posB]
        data[posC] = result
        pos += 4


def find_noun_verb(raw_data, output):
    result = run_intcode(raw_data)
    if result[0] == output:
        return None
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run_intcode(raw_data, noun, verb)
            if result[0] == output:
                return 100 * noun + verb
    return None


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    data = run_intcode(raw_data, 12, 2)
    print('Output: {0}'.format(data[0]))
    result = find_noun_verb(raw_data, 19690720)
    print('Noun/Verb that produces {0}: {1}'.format(19690720, result))
