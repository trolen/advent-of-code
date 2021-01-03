#! /usr/bin/env python3

DIRECTIONS = '<^>v'


class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self._intersections = 0

    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y == other.y and self.x < other.x:
            return True
        return False

    def __repr__(self):
        return 'Cart()'

    def __str__(self):
        return str((self.x, self.y, self.direction))

    def move(self):
        if self.direction == '>':
            self.x += 1
        elif self.direction == '<':
            self.x -= 1
        elif self.direction == 'v':
            self.y += 1
        else:  # self.direction == '^'
            self.y -= 1

    def turn_left(self):
        idx = DIRECTIONS.index(self.direction)
        idx = (idx + 3) % 4
        self.direction = DIRECTIONS[idx]

    def turn_right(self):
       idx = DIRECTIONS.index(self.direction)
       idx = (idx + 1) % 4
       self.direction = DIRECTIONS[idx]

    def intersection(self):
        if self._intersections == 0:
            self.turn_left()
        if self._intersections == 2:
            self.turn_right()
        self._intersections = (self._intersections + 1) % 3


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._parse_data()

    def _parse_data(self):
        self._grid = []
        self._carts = []
        for y in range(0, len(self._raw_data)):
            data_row = self._raw_data[y]
            row = ''
            for x in range(0, len(data_row)):
                ch = data_row[x]
                if ch not in DIRECTIONS:
                    row += ch
                    continue
                self._carts.append(Cart(x, y, ch))
                if ch in '<>':
                    row += '-'
                    continue
                row += '|'
            self._grid.append(row)

    def _did_crash(self, idx0):
        found = None
        cart0 = self._carts[idx0]
        for idx in range(0, len(self._carts)):
            if idx == idx0:
                continue
            cart = self._carts[idx]
            if cart.x == cart0.x and cart.y == cart0.y:
                found = idx
                break
        return found

    def _tick(self, delete_crashed_carts=False):
        self._carts.sort()
        n_carts = len(self._carts)
        idx = 0
        while idx < n_carts:
            cart = self._carts[idx]
            cart.move()
            idx1 = self._did_crash(idx)
            if idx1 is not None:
                if not delete_crashed_carts:
                    return (cart.x, cart.y)
                del self._carts[idx1]
                if idx1 < idx:
                    idx -= 1
                del self._carts[idx]
                n_carts = len(self._carts)
                continue
            ch = self._grid[cart.y][cart.x]
            if ch == '+':
                cart.intersection()
            elif (ch == '/' and cart.direction in 'v^') or (ch == '\\' and cart.direction in '<>'):
                cart.turn_right()
            elif (ch == '/' and cart.direction in '<>') or (ch == '\\' and cart.direction in 'v^'):
                cart.turn_left()
            idx += 1
        if n_carts == 1:
            return (self._carts[0].x, self._carts[0].y)
        return None

    def do_part1(self):
        result = None
        while result is None:
            result = self._tick()
        return result

    def do_part2(self):
        self._parse_data()
        result = None
        while result is None:
            result = self._tick(delete_crashed_carts=True)
        return result

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.rstrip('\n') for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
