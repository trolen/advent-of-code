#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return int(file.readline().strip())


def calc_power_level(x, y, serial):
    rack_id = x + 10
    power_level = ((rack_id * y) + serial) * rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level


def build_grid(serial):
    grid = []
    for y in range(0, 300):
        row = []
        for x in range(0, 300):
            row.append(calc_power_level(x+1, y+1, serial))
        grid.append(row)
    return grid


def find_largest_power_by_size(grid, size=3):
    outer_range = 300 - size
    powers_by_size = {}
    for yTop in range(0, outer_range):
        for xLeft in range(0, outer_range):
            pwr = sum([sum(grid[yTop + y][xLeft:xLeft+size]) for y in range(0, size)])
            powers_by_size[pwr] = (xLeft + 1, yTop + 1)
    max_power = max(powers_by_size.keys())
    point = powers_by_size[max_power]
    return (point[0], point[1], max_power)


def find_largest_power_any_size(grid):
    max_powers_by_size = {}
    for size in range(0, 300):
        (x, y, pwr) = find_largest_power_by_size(grid, size)
        max_powers_by_size[pwr] = (x, y, size)
    max_power = max(max_powers_by_size.keys())
    return max_powers_by_size[max_power]


if __name__ == '__main__':
    data = read_data('input.txt')
    grid = build_grid(data)
    point = find_largest_power_by_size(grid)
    print('3x3 Square with Largest Power at: {0},{1}'.format(point[0], point[1]))
    point = find_largest_power_any_size(grid)
    print('{2}x{2} Square with Largest Power at: {0},{1}'.format(point[0], point[1], point[2]))
