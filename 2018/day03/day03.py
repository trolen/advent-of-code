#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_data_lines(input):
    data = {}
    for line in input:
        (id, s) = line.split('@')
        id = int(id[1:])
        (coords, dims) = s.split(':')
        (left, top) = coords.split(',')
        (width, height) = dims.split('x')
        data[id] = {
            'id': id,
            'left': int(left),
            'top': int(top),
            'width': int(width),
            'height': int(height)
        }
    return data


def build_grid(data):
    grid = []
    for i in range(0, 1000):
        grid.append(['.'] * 1000)
    for key in data:
        row = data[key]
        for c in range(row['left'], row['left']+row['width']):
            for r in range(row['top'], row['top']+row['height']):
                if isinstance(grid[r][c], int):
                    grid[r][c] = 'X'
                elif grid[r][c] == '.':
                    grid[r][c] = row['id']
    return grid


def count_overlap(grid):
    cnt = 0
    for r in range(0, 1000):
        for c in range(0, 1000):
            if isinstance(grid[r][c], str) and grid[r][c] == 'X':
                cnt += 1
    return cnt


def find_non_overlap(data, grid):
    for key in data:
        row = data[key]
        overlap = False
        for c in range(row['left'], row['left']+row['width']):
            for r in range(row['top'], row['top']+row['height']):
                if isinstance(grid[r][c], str) and grid[r][c] == 'X':
                    overlap = True
                    break
            if overlap:
                break
        if not overlap:
            return key
    return None


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    data = parse_data_lines(raw_data)
    grid = build_grid(data)
    cnt = count_overlap(grid)
    print('Overlap: {0}'.format(cnt))
    id = find_non_overlap(data, grid)
    print('Non Overlap ID: {0}'.format(id))