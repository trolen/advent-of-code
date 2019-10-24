#! /usr/bin/env python3

class Point:
    def __init__(self, position, velocity):
        self._x = position[0]
        self._y = position[1]
        self._vel_x = velocity[0]
        self._vel_y = velocity[1]

    def move(self):
        self._x += self._vel_x
        self._y += self._vel_y

    def reverse(self):
        self._x -= self._vel_x
        self._y -= self._vel_y

    def position(self):
        return (self._x, self._y)


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_data(raw_data):
    results = []
    for line in raw_data:
        s = line.replace('position=<', '').replace('velocity=<', '').replace(',', '', 2).replace('>', '', 2)
        terms = s.split()
        p = (int(terms[0]), int(terms[1]))
        v = (int(terms[2]), int(terms[3]))
        results.append(Point(p, v))
    return results


def move_points(data):
    for point in data:
        point.move()


def reverse_points(data):
    for point in data:
        point.reverse()


def calc_dimensions(data):
    min_x = None
    max_x = None
    min_y = None
    max_y = None
    for point in data:
        pos = point.position()
        if min_x is None or pos[0] < min_x:
            min_x = pos[0]
        if max_x is None or pos[0] > max_x:
            max_x = pos[0]
        if min_y is None or pos[1] < min_y:
            min_y = pos[1]
        if max_y is None or pos[1] > max_y:
            max_y = pos[1]
    return (min_x, max_x, min_y, max_y)


def calc_area(data):
    (min_x, max_x, min_y, max_y) = calc_dimensions(data)
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    return len_x * len_y


def show_grid(data):
    (min_x, max_x, min_y, max_y) = calc_dimensions(data)
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    print('\n========================')
    for j in range(0, len_y):
        y = min_y + j
        row = ''
        for i in range(0, len_x):
            x = min_x + i
            found = False
            for point in data:
                pos = point.position()
                if x == pos[0] and y == pos[1]:
                    found = True
                    break
            row += '#' if found else '.'
        print(row)
    print('========================')


def animate_points(data):
    a0 = calc_area(data)
    cnt = 0
    while True:
        move_points(data)
        a1 = calc_area(data)
        if a1 > a0:
            reverse_points(data)
            break
        a0 = a1
        cnt += 1
    return cnt


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    data = parse_data(raw_data)
    cnt = animate_points(data)
    show_grid(data)
    print('Seconds: {0}'.format(cnt))
