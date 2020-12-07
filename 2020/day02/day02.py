#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_data(raw_data):
    result = []
    for line in raw_data:
        terms = line.split()
        limits = terms[0].split("-")
        ch = terms[1]
        pwd = terms[2]
        entry = {}
        entry['lower'] = int(limits[0])
        entry['upper'] = int(limits[1])
        entry['char'] = ch[0]
        entry['password'] = pwd
        result.append(entry)
    return result

def is_valid1(entry):
    cnt = entry['password'].count(entry['char'])
    return entry['lower'] <= cnt and cnt <= entry['upper']

def is_valid2(entry):
    lower_ch = entry['password'][entry['lower'] - 1]
    upper_ch = entry['password'][entry['upper'] - 1]
    lower_match = lower_ch == entry['char']
    upper_match = upper_ch == entry['char']
    if lower_match or upper_match:
        return lower_match != upper_match
    return False

def count_valid_pwds(pwd_list, method):
    result = 0
    for entry in pwd_list:
        if method == 1 and is_valid1(entry):
            result += 1
            continue
        if method == 2 and is_valid2(entry):
            result += 1
    return result

def do_part1(pwd_list):
    return count_valid_pwds(pwd_list, 1)

def do_part2(pwd_list):
    return count_valid_pwds(pwd_list, 2)

def execute():
    raw_data = read_data('input.txt')
    pwd_list = parse_data(raw_data)
    print('Part 1 result: ', do_part1(pwd_list))
    print('Part 2 result: ', do_part2(pwd_list))

if __name__ == '__main__':
    execute()
