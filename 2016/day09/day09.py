#! /usr/bin/env python3


def get_length1(s):
    result = 0
    marker = ''
    in_marker = False
    in_repeat = False
    num_chars = 0
    for ch in s:
        if in_marker:
            if ch == 'x':
                num_chars = int(marker)
                marker = ''
            elif ch == ')':
                in_marker = False
                in_repeat = True
                result += num_chars * int(marker)
                marker = ''
            else:
                marker += ch
        elif in_repeat:
            num_chars -= 1
            if num_chars <= 0:
                in_repeat = False
        elif ch == '(':
            marker = ''
            in_marker = True
        else:
            result += 1
    return result


def get_length2(s):
    result = 0
    marker = ''
    in_marker = False
    in_repeat = False
    num_chars = 0
    num_repeat = 0
    repeat_chars = ''
    for ch in s:
        if in_marker:
            if ch == 'x':
                num_chars = int(marker)
                marker = ''
            elif ch == ')':
                in_marker = False
                in_repeat = True
                num_repeat = int(marker)
                marker = ''
            else:
                marker += ch
        elif in_repeat:
            repeat_chars += ch
            num_chars -= 1
            if num_chars <= 0:
                result += num_repeat * get_length2(repeat_chars)
                in_repeat = False
                repeat_chars = ''
        elif ch == '(':
            marker = ''
            in_marker = True
        else:
            result += 1
    return result


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    print('Part One: {0}'.format(sum([get_length1(line) for line in data])))
    print('Part Two: {0}'.format(sum([get_length2(line) for line in data])))