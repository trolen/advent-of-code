#! /usr/bin/env python3

def decode_column(data, col):
    letters = {}
    for row in data:
        if row[col] not in letters:
            letters[row[col]] = 0
        letters[row[col]] += 1
    return letters


def most_freq_letter(data, col):
    letters = decode_column(data, col)
    most_freq = ''
    count = 0
    for letter in letters:
        if letters[letter] > count:
            count = letters[letter]
            most_freq = letter
    return most_freq


def least_freq_letter(data, col):
    letters = decode_column(data, col)
    least_freq = ''
    count = 99
    for letter in letters:
        if letters[letter] < count:
            count = letters[letter]
            least_freq = letter
    return least_freq


def decode_message1(data, n):
    message = ''
    for col in range(n):
        message += most_freq_letter(data, col)
    return message


def decode_message2(data, n):
    message = ''
    for col in range(n):
        message += least_freq_letter(data, col)
    return message


def read_data(filename):
    data = []
    with open(filename, 'rt') as file:
        for line in file:
            data.append(line.strip())
    return data


if __name__ == '__main__':
    data = read_data('input.txt')
    print('Part One: {0}'.format(decode_message1(data, 8)))
    print('Part Two: {0}'.format(decode_message2(data, 8)))