#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._instructions = raw_data

    def _reset(self, method=1):
        self._method = method
        self._ship = (0, 0)
        self._waypoint = (1, 0) if method == 1 else (10, 1)

    def _move(self, direction, distance):
        if self._method == 1:
            (x, y) = self._ship
        elif self._method == 2:
            (x, y) = self._waypoint
        if direction == 'N':
            y += distance
        elif direction == 'S':
            y -= distance
        elif direction == 'E':
            x += distance
        elif direction == 'W':
            x -= distance
        if self._method == 1:
            self._ship = (x, y)
        elif self._method == 2:
            self._waypoint = (x, y)

    def _forward(self, distance):
        (x, y) = self._ship
        (dx, dy) = self._waypoint
        for i in range(0, distance):
            x += dx
            y += dy
        self._ship = (x, y)

    def _turn(self, direction, angle):
        if direction == 'R':
            angle = 360 - angle
        (x, y) = self._waypoint
        if angle == 90:
            (x, y) = (-y, x)
        elif angle == 180:
            (x, y) = (-x, -y)
        elif angle == 270:
            (x, y) = (y, -x)
        self._waypoint = (x, y)

    def _process_instructions(self):
        for instruction in self._instructions:
            action = instruction[0]
            arg = int(instruction[1:])
            if action in 'NSEW':
                self._move(action, arg)
            elif action in 'LR':
                self._turn(action, arg)
            elif action == 'F':
                self._forward(arg)

    def _manhattan_distance(self):
        (x, y) = self._ship
        return abs(x) + abs(y)

    def do_part1(self):
        self._reset(1)
        self._process_instructions()
        return self._manhattan_distance()

    def do_part2(self):
        self._reset(2)
        self._process_instructions()
        return self._manhattan_distance()

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
