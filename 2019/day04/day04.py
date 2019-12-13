#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def parse_data(raw_data):
    return [int(x) for x in raw_data.split('-')]


def get_digits(pw):
    s = str(pw)
    result = []
    for ch in s:
        result.append(int(ch))
    return result


def is_valid_pw(pw, no_triples=False):
    digits = get_digits(pw)
    repeat_digit = False
    for i in range(1, len(digits)):
        if digits[i] < digits[i - 1]:
            return False
        if digits[i] == digits[i - 1]:
            if no_triples:
                if i > 1 and digits[i] == digits[i - 2]:
                    continue
                if i < len(digits) - 1 and digits[i] == digits[i + 1]:
                    continue
            repeat_digit = True
    return repeat_digit


def find_valid_passwords(start, end):
    result = []
    for pw in range(start, end+1):
        if is_valid_pw(pw):
            result.append(pw)
    return result


def find_valid_passwords_without_triples(passwords):
    result = []
    for pw in passwords:
        if is_valid_pw(pw, no_triples=True):
            result.append(pw)
    return result


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    (start, end) = parse_data(raw_data)
    passwords = find_valid_passwords(start, end)
    print('Valid passwords: {0}'.format(len(passwords)))
    pw_without_triples = find_valid_passwords_without_triples(passwords)
    print('Valid passwords without triples: {0}'.format(len(pw_without_triples)))
