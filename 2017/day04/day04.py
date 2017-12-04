#! /usr/bin/env python3

from collections import Counter

def is_valid1(phrase):
    counter = Counter(phrase.split())
    for key in counter:
        if counter[key] > 1:
            return False
    return True

def is_anagram(word1, word2):
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    if len(counter1.keys()) != len(counter2.keys()):
        return False
    for key in counter1.keys():
        if key not in counter2.keys():
            return False
        if counter1[key] != counter2[key]:
            return False
    return True

def is_valid2(phrase):
    words = phrase.split()
    for idx1 in range(len(words) - 1):
        for idx2 in range(idx1 + 1, len(words)):
            if is_anagram(words[idx1], words[idx2]):
                return False
    return True

def count_valid_phrases(data, part2=False):
    result = 0
    for phrase in data:
        if is_valid1(phrase):
            if part2 and not is_valid2(phrase):
                continue
            result += 1
    return result

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    print('Part One: {0}'.format(count_valid_phrases(data)))
    print('Part Two: {0}'.format(count_valid_phrases(data, part2=True)))
