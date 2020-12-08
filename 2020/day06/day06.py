#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_data(raw_data):
    result = []
    group = []
    for line in raw_data:
        if len(line) == 0:
            result.append(group)
            group = []
            continue
        group.append(line)
    if len(group) > 0:
        result.append(group)
    return result

def get_unique_chars(group):
    result = []
    for s in group:
        for ch in s:
            if ch not in result:
                result.append(ch)
    return ''.join(sorted(result))

def get_common_chars(group):
    old_result = 'abcdefghijklmnopqrstuvwxyz'
    for s in group:
        result = []
        for ch in s:
            if ch in old_result:
                result.append(ch)
        old_result = ''.join(result)
    return ''.join(sorted(result))

def do_part1(groups):
    counts = []
    for group in groups:
        s = get_unique_chars(group)
        counts.append(len(s))
    return sum(counts)

def do_part2(groups):
    counts = []
    for group in groups:
        s = get_common_chars(group)
        counts.append(len(s))
    return sum(counts)

def execute():
    raw_data = read_data('input.txt')
    groups = parse_data(raw_data)
    print('Part 1 result:', do_part1(groups))
    print('Part 2 result:', do_part2(groups))

if __name__ == '__main__':
    execute()