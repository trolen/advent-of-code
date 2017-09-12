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


def is_aba(s):
    if len(s) != 3:
        return False
    if s[0] == s[1]:
        return False
    if s[0] == s[2]:
        return True
    return False


def find_aba(s):
    result = []
    if len(s) < 3:
        return result
    stop = len(s) - 2
    for idx in range(stop):
        s_test = s[idx:idx+3]
        if is_aba(s_test):
            result.append(s_test)
    return result


def supports_ssl(s):
    find_this = '['
    start = 0
    end = 0
    aba_outside = []
    aba_inside = []
    while end != -1:
        end = s.find(find_this, start)
        result = find_aba(s[start:end if end != -1 else len(s)])
        if find_this == '[':
            aba_outside.extend(result)
        else:
            aba_inside.extend(result)
        start = end + 1
        find_this = ']' if find_this == '[' else '['
    for aba in aba_outside:
        bab = aba[1] + aba[0] + aba[1]
        if bab in aba_inside:
            return True
    return False


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
    count = 0
    for line in data:
        if supports_ssl(line):
            count += 1
    print('Part Two: {0}'.format(count))
