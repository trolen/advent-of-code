#! /usr/bin/env python3


def is_triangle(sides):
    s = sorted(sides)
    return (s[0] + s[1]) > s[2]


if __name__ == '__main__':
    with open('input.txt', 'rt') as file:
        lines = file.readlines()
    sides = []
    for line in lines:
        sides.append([int(x) for x in line.strip().split()])
    count = 0
    for t in sides:
        if is_triangle(t):
            count += 1
    print('Part One: {0}'.format(count))
    count = 0
    for i in range(0, len(sides), 3):
        for j in range(3):
            t = [sides[i][j], sides[i+1][j], sides[i+2][j]]
            if is_triangle(t):
                count += 1
    print('Part Two: {0}'.format(count))
