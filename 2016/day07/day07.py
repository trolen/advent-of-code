#! /usr/bin/env python3


def is_abba(s):
    if len(s) != 4:
        return False
    if s[0] == s[1]:
        return False
    if s[0] == s[3] and s[1] == s[2]:
        return True
    return False


def contains_abba(s):
    if len(s) < 4:
        return False
    stop = len(s) - 3
    for idx in range(stop):
        if is_abba(s[idx:idx+4]):
            return True
    return False


def supports_tls(s):
    find_this = '['
    start = 0
    end = 0
    abba_outside = False
    abba_inside = False
    while end != -1:
        end = s.find(find_this, start)
        if contains_abba(s[start:end if end != -1 else len(s)]):
            if find_this == '[':
                abba_outside = True
            else:
                abba_inside = True
        start = end + 1
        find_this = ']' if find_this == '[' else '['
    return abba_outside and not abba_inside


def read_data(filename):
    data = []
    with open(filename, 'rt') as file:
        data = [line.strip() for line in file]
    return data


if __name__ == '__main__':
    data = read_data('input.txt')
    count = 0
    for line in data:
        if supports_tls(line):
            count += 1
    print('Part One: {0}'.format(count))