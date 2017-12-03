#! /usr/bin/env python3

def sum_pairs(s, part2=False):
    n = len(s)
    result = 0
    for i1 in range(n):
        if part2:
            incr = n//2
        else:
            incr = 1
        i2 = (i1 + incr) % n
        if s[i1] == s[i2]:
            result += int(s[i1])
    return result

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline()

if __name__ == '__main__':
    data = read_data('input.txt')
    print('Part One: {0}'.format(sum_pairs(data)))
    print('Part Two: {0}'.format(sum_pairs(data, True)))
