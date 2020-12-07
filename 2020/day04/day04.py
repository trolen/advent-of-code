#! /usr/bin/env python3

import re

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

FOURDIGITS = re.compile('^\d{4}$')
HGT = re.compile('^\d+(in|cm)$')
HCL = re.compile('^#[0-9a-f]{6}$')
NINEDIGITS = re.compile('^\d{9}$')

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

def parse_data(raw_data):
    result = []
    passport = {}
    for line in raw_data:
        if len(line) == 0:
            result.append(passport)
            passport = {}
            continue
        fields = line.split()
        for field in fields:
            items = field.split(":")
            passport[items[0]] = items[1]
    if len(passport) > 0:
        result.append(passport)
    return result

def is_valid_byr(value):
    if re.match(FOURDIGITS, value) is None:
        return False
    n = int(value)
    return 1920 <= n and n <= 2002

def is_valid_iyr(value):
    if re.match(FOURDIGITS, value) is None:
        return False
    n = int(value)
    return 2010 <= n and n <= 2020

def is_valid_eyr(value):
    if re.match(FOURDIGITS, value) is None:
        return False
    n = int(value)
    return 2020 <= n and n <= 2030

def is_valid_hgt(value):
    if re.match(HGT, value) is None:
        return False
    unit = value[-2:]
    n = int(value[:-2])
    if unit == 'cm':
        return 150 <= n and n <= 193
    if unit == 'in':
        return 59 <= n and n <= 76
    return False

def is_valid_hcl(value):
    return re.match(HCL, value) is not None

def is_valid_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def is_valid_pid(value):
    return re.match(NINEDIGITS, value) is not None

def is_valid(passport, data_validation = False):
    for fld in required_fields:
        if fld not in passport:
            return False
        value = passport[fld]
        if data_validation:
            if fld == 'byr' and not is_valid_byr(value):
                return False
            if fld == 'iyr' and not is_valid_iyr(value):
                return False
            if fld == 'eyr' and not is_valid_eyr(value):
                return False
            if fld == 'hgt' and not is_valid_hgt(value):
                return False
            if fld == 'hcl' and not is_valid_hcl(value):
                return False
            if fld == 'ecl' and not is_valid_ecl(value):
                return False
            if fld == 'pid' and not is_valid_pid(value):
                return False
    return True

def do_part1(passports):
    result = 0
    for passport in passports:
        if is_valid(passport):
            result += 1
    return result

def do_part2(passports):
    result = 0
    for passport in passports:
        if is_valid(passport, True):
            result += 1
    return result

def execute():
    raw_data = read_data('input.txt')
    passports = parse_data(raw_data)
    print('Part 1 result:', do_part1(passports))
    print('Part 2 result:', do_part2(passports))

if __name__ == '__main__':
    execute()