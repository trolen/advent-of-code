#! /usr/bin/env python3

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N, E, S, W

class Position:
    def __init__(self):
        self.reset()

    def reset(self):
        self._x, self._y = (0, 0)
        self._direction = 0
        self._positions = []

    def get_distance(self):
        return abs(self._x) + abs(self._y)

    def apply_instruction(self, instruction, unique):
        turn = instruction[0].upper()
        if turn == 'R':
            self._direction += 1
        else:
            self._direction -= 1
        self._direction %= 4
        distance = int(instruction[1:])
        if not unique:
            self._x += DIRECTIONS[self._direction][0] * distance
            self._y += DIRECTIONS[self._direction][1] * distance
            return False
        if DIRECTIONS[self._direction][0] != 0:
            plist = [(self._x + i * DIRECTIONS[self._direction][0], self._y) for i in range(1, distance + 1)]
        if DIRECTIONS[self._direction][1] != 0:
            plist = [(self._x, self._y + i * DIRECTIONS[self._direction][1]) for i in range(1, distance + 1)]
        for p in plist:
            self._x, self._y = p
            if p in self._positions:
                return True
            self._positions.append(p)
        return False

    def apply_instructions(self, instructions, unique=False):
        for instruction in [x.strip() for x in instructions.split(',')]:
            if self.apply_instruction(instruction, unique):
                break


if __name__ == '__main__':
    instructions = ''
    with open('input.txt', 'rt') as file:
        instructions = file.read()
    p = Position()
    p.apply_instructions(instructions)
    print('Part One: {0}'.format(p.get_distance()))
    p.reset()
    p.apply_instructions(instructions, unique=True)
    print('Part Two: {0}'.format(p.get_distance()))