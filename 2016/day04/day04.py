#! /usr/bin/env python3

from collections import OrderedDict


def parse_name(encrypted_name):
    parts = encrypted_name.split('-')
    letters = '-'.join(parts[:-1])
    num, checksum_str = parts[-1].split('[')
    id_num = int(num)
    checksum = checksum_str[:-1]
    return letters, id_num, checksum


def tally_letters(letters):
    tally = {}
    for ch in letters:
        if ch == '-':
            continue
        cnt = 0
        if ch in tally:
            cnt = tally[ch]
        cnt += 1
        tally[ch] = cnt
    return OrderedDict(sorted(sorted(tally.items(), key=lambda x: x[0]), key=lambda y: y[1], reverse=True))


def build_checksum(tally, num):
    result = ''
    i = 0
    for item in tally:
        result += item[0]
        i += 1
        if i >= num:
            break
    return result


def decode_name(encrypted_name):
    name, id_num, checksum = parse_name(encrypted_name)
    sorted_tally = tally_letters(name)
    if build_checksum(sorted_tally, 5) == checksum:
        decoded_name = ''
        for ch in name:
            if ch == '-':
                ch = ' '
            else:
                n = ord(ch) - ord('a')
                n += id_num
                n %= 26
                ch = chr(ord('a') + n)
            decoded_name += ch
    else:
        id_num = 0
        decoded_name = name
    return decoded_name, id_num


def read_data(filename):
    with open(filename, 'rt') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


if __name__ == '__main__':
    room_names = read_data('input.txt')
    name_info = [decode_name(name) for name in room_names]
    total = sum([item[1] for item in name_info])
    print('Part One: {0}'.format(total))
    for item in name_info:
        if 'north' in item[0]:
            print('Part Two: {0}:'.format(item))
            break
