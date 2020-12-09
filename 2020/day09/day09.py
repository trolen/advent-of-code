#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_data(raw_data):
    return [int(line) for line in raw_data]

def is_valid(number_list, preamble, idx):
    for i in range(idx - preamble, idx - 1):
        for j in range(i + 1, idx):
            if number_list[i] + number_list[j] == number_list[idx]:
                return True
    return False

def do_part1(number_list, preamble):
    for i in range(preamble, len(number_list)):
        if not is_valid(number_list, preamble, i):
            return number_list[i]
    return -1

def do_part2(number_list, key):
    for i in range(0, len(number_list) - 1):
        smallest = number_list[i]
        largest = number_list[i]
        sum_of_range = number_list[i]
        for j in range(i + 1, len(number_list)):
            smallest = min(smallest, number_list[j])
            largest = max(largest, number_list[j])
            sum_of_range += number_list[j]
            if sum_of_range > key:
                break
            if sum_of_range == key:
                return smallest + largest
    return -1

def execute():
    raw_data = read_data('input.txt')
    number_list = parse_data(raw_data)
    key = do_part1(number_list, 25)
    print('Part 1 result:', key)
    print('Part 2 result:', do_part2(number_list, key))

if __name__ == '__main__':
    execute()
