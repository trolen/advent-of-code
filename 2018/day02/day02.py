#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [x.strip() for x in file.readlines()]


def calc_checksum(data):
    num_two = 0
    num_three = 0
    for s in data:
        unique_chars = sorted(set(s))
        found_two = False
        found_three = False
        for ch in unique_chars:
            cnt = s.count(ch)
            if cnt == 2:
                found_two = True
            if cnt == 3:
                found_three = True
        if found_two:
            num_two += 1
        if found_three:
            num_three += 1
    return num_two * num_three


def is_match(s1, s2):
    diffs = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            diffs += 1
            if diffs > 1:
                return False
    return True


def find_matches(data):
    matches = []
    for i in range(0, len(data) - 1):
        for j in range(i + 1, len(data)):
            if is_match(data[i], data[j]):
                return (i,j)
    return None


def find_matching_string(data):
    matches = find_matches(data)
    if matches is None:
        return None
    s1 = data[matches[0]]
    s2 = data[matches[1]]
    result = ''
    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
    return result


if __name__ == '__main__':
    data = read_data('input.txt')
    checksum = calc_checksum(data)
    print('Checksum: {0}'.format(checksum))
    matching_string = find_matching_string(data)
    print('Mathing String: {0}'.format(matching_string))