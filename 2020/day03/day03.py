#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def count_trees(raw_data, slope_x, slope_y):
    x = 0
    y = 0
    result = 0
    while y < len(raw_data):
        row = raw_data[y]
        if row[x] == '#':
            result += 1
        x += slope_x
        x = x % len(row)
        y += slope_y
    return result

def do_part1(raw_data):
    return count_trees(raw_data, 3, 1)

def do_part2(raw_data):
    slopes = [
        [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]
    ]
    result = 1
    for slope in slopes:
        n = count_trees(raw_data, slope[0], slope[1])
        result *= n
    return result

def execute():
    raw_data = read_data('input.txt')
    print('Part 1 result:', do_part1(raw_data))
    print('Part 2 result:', do_part2(raw_data))

if __name__ == '__main__':
    execute()
