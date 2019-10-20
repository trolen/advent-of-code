#! /usr/bin/env python3

from datetime import datetime

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_points(data):
    points = []
    for sCoords in data:
        (x, y) = sCoords.split(',')
        points.append((int(x), int(y)))
    return points


def get_grid_dimensions(points):
    max_x = 0
    max_y = 0
    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    max_x += 1
    max_y += 1
    return (max_x, max_y)


def manhattan_distance(p1, p2):
    n1 = abs(p2[0] - p1[0])
    n2 = abs(p2[1] - p1[1])
    return n1 + n2


def build_grid_with_areas(points):
    (max_x, max_y) = get_grid_dimensions(points)
    grid = []
    for y in range(0, max_y):
        row = []
        for x in range(0, max_x):
            min_distance = None
            point_idx = None
            for i in range(0, len(points)):
                point = points[i]
                if point[0] == x and point[1] == y:
                    min_distance = 0
                    point_idx = i
                    break
                d = manhattan_distance(point, (x,y))
                if min_distance is None or d < min_distance:
                    min_distance = d
                    point_idx = i
                elif d == min_distance:
                    point_idx = -1
            row.append(point_idx)
        grid.append(row)
    return grid


def find_edge_points(grid):
    results = []
    n_rows = len(grid)
    for i in range(0, n_rows):
        n_cols = len(grid[i])
        for j in range(0, n_cols):
            n = grid[i][j]
            if n == -1:
                continue
            if n in results:
                continue
            if i == 0 or j == 0 or i == n_rows - 1 or j == n_cols - 1:
                results.append(n)
    return results


def find_largest_non_infinite_area(points, grid):
    edge_points = find_edge_points(grid)
    results = {}
    n_rows = len(grid)
    for i in range(0, n_rows):
        n_cols = len(grid[i])
        for j in range(0, n_cols):
            n = grid[i][j]
            if n == -1 or n in edge_points:
                continue
            if n not in results:
                results[n] = 0
            results[n] = results[n] + 1
    max_area = 0
    for key in results:
        n = results[key]
        if n > max_area:
            max_area = n
    return max_area


def find_area_within_distance(points, grid, dist):
    result = 0
    len_y = len(grid)
    for y in range(0, len_y):
        len_x = len(grid[y])
        for x in range(0, len_x):
            distances = []
            for point in points:
                distances.append(manhattan_distance((x,y), point))
            if sum(distances) < dist:
                result += 1
    return result


if __name__ == '__main__':
    data = read_data('input.txt')
    points = parse_points(data)
    grid = build_grid_with_areas(points)
    a = find_largest_non_infinite_area(points, grid)
    print('Largest non-infinite area: {0}'.format(a))
    a = find_area_within_distance(points, grid, 10000)
    print('Area with distance < 10000: {0}'.format(a))
