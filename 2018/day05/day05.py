#! /usr/bin/env python3

from datetime import datetime

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def process_reactions(data):
    result = ''
    for ch in data:
        if len(result) == 0:
            result += ch
            continue
        prev_char = result[-1]
        ch_to_compare = prev_char.lower()
        if prev_char.islower():
            ch_to_compare = prev_char.upper()
        if ch == ch_to_compare:
            result = result[:-1]
            continue
        result += ch
    if result == data:
        return result
    return process_reactions(result)


def find_shortest_polymer(data):
    shortest_polymer = None
    shortest_length = None
    for i in range(0, 26):
        ch1 = chr(ord('a') + i)
        ch2 = chr(ord('A') + i)
        reduced_data = ''.join([ch for ch in data if ch not in (ch1, ch2)])
        if reduced_data == data:
            continue
        polymer = process_reactions(reduced_data)
        polymer_length = len(polymer)
        if shortest_length is None or polymer_length < shortest_length:
            shortest_polymer = polymer
            shortest_length = polymer_length
    return shortest_polymer


if __name__ == '__main__':
    data = read_data('input.txt')
    s = process_reactions(data)
    print('Units remaining: {0}'.format(len(s)))
    s = find_shortest_polymer(data)
    print('Units of shortest polymer: {0}'.format(len(s)))
