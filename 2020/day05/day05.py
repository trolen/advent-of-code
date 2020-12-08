#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]

def parse_line(line):
    rMin = 0
    rMax = 127
    cMin = 0
    cMax = 7
    for i in range(0, len(line)):
        ch = line[i]
        rMid = rMin + (rMax - rMin + 1) / 2
        cMid = cMin + (cMax - cMin + 1) / 2
        if ch == 'F':
            rMax = rMid - 1
        if ch == 'B':
            rMin = rMid
        if ch == 'L':
            cMax = cMid - 1
        if ch == 'R':
            cMin = cMid
    id = rMin * 8 + cMin
    return int(id)

def parse_data(raw_data):
    result = []
    for line in raw_data:
        result.append(parse_line(line))
    return result

def do_part1(seat_numbers):
    return max([id for id in seat_numbers])

def do_part2(seat_numbers):
    sorted_numbers = sorted(seat_numbers)
    for i in range(0, len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        if diff > 1:
            return sorted_numbers[i] + 1
    return 0

def execute():
    raw_data = read_data('input.txt')
    seat_numbers = parse_data(raw_data)
    print('Part 1 result:', do_part1(seat_numbers))
    print('Part 2 result:', do_part2(seat_numbers))

if __name__ == '__main__':
    execute()
