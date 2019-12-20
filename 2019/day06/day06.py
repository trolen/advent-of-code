#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_orbits(raw_data):
    return [line.split(')') for line in raw_data]


def navigate_to_com(orbits, start):
    for o in orbits:
        if o[1] == start:
            if o[0] == 'COM':
                return 1
            return 1 + navigate_to_com(orbits, o[0])
    return None


def count_orbits(orbits):
    result = 0
    for o in orbits:
        result += navigate_to_com(orbits, o[1])
    return result


def find_santa(orbits, next, prev=None):
    for o in orbits:
        if next == 'YOU':
            if o[1] == next:
                return find_santa(orbits, o[0], next)
            continue
        if o[0] == next and o[1] == 'SAN':
            return 0
        next_find = None
        if o[0] == next and not o[1] == prev:
            next_find = o[1]
        if o[1] == next and not o[0] == prev:
            next_find = o[0]
        if next_find is not None:
            result = find_santa(orbits, next_find, next)
            if result is not None:
                return 1 + result
    return None


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    orbits = parse_orbits(raw_data)
    cnt = count_orbits(orbits)
    print('Orbit count: {0}'.format(cnt))
    cnt = find_santa(orbits, 'YOU')
    print('Steps to Santa: {0}'.format(cnt))
