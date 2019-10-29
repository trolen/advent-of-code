#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_data(data):
    rules = {}
    for line in data:
        if len(line) == 0:
            continue
        if 'initial state: ' in line:
            initial_state = line[15:]
            continue
        key = line[:5]
        rules[key] = line[9]
    return (initial_state, rules)


def next_generation(prev_generation, rules, zero_offset):
    n1 = 4 - prev_generation.find('#')
    if n1 < 0:
        n1 = 0
    n2 = 4 - (len(prev_generation) - 1 - prev_generation.rfind('#'))
    if n2 < 0:
        n2 = 0
    n_start = 0 - n1
    n_end = len(prev_generation) - 4 + n2
    result = ''
    if n_start < 0:
        for i in range(n_start, 0):
            n = abs(i)
            s = '.'*n + prev_generation[:5-n]
            if s in rules.keys():
                result += rules[s]
            else:
                result += '.'
    n3 = len(prev_generation) - 4
    if n_end < n3:
        n3 = n_end
    for i in range(0, n3):
        s = prev_generation[i:i+5]
        if s in rules.keys():
            result += rules[s]
        else:
            result += '.'
    if n_end > n3:
        for i in range(n3, n_end):
            n = 5 + i - len(prev_generation)
            s = prev_generation[i:] + '.'*n
            if s in rules.keys():
                result += rules[s]
            else:
                result += '.'
    return (result, zero_offset + n1 - 2)


def calc_score(cur_generation, zero_offset):
    result = 0
    for i in range(0, len(cur_generation)):
        if cur_generation[i] == '#':
            result += i - zero_offset
    return result


def calc_score_after_generations(data, n_generations):
    (cur_state, rules) = parse_data(data)
    zero_offset = 0
    for i in range(0, n_generations):
        (cur_state, zero_offset) = next_generation(cur_state, rules, zero_offset)
        if i % 100000 == 0:
            print('\r{0}\r{1}: '.format(' '*75, i), end='')
        if i % 10000 == 0:
            print('.', end='', flush=True)
    print()
    return calc_score(cur_state, zero_offset)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    score = calc_score_after_generations(raw_data, 20)
    print('Score after 20 generations: {0}'.format(score))
    score = calc_score_after_generations(raw_data, 50000000000)
    print('Score after 50000000000 generations: {0}'.format(score))
