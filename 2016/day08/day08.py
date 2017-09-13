#! /usr/bin/env python3

class Screen:
    def __init__(self, width, height):
        self._screen = []
        for r in range(height):
            self._screen.append([0 for c in range(width)])

    def rows(self):
        for r in range(len(self._screen)):
            yield r

    def columns(self):
        for c in range(len(self._screen[0])):
            yield c

    def show(self):
        result = []
        for r in self.rows():
            result.append('')
            for c in self.columns():
                result[r] += '#' if self._screen[r][c] else '.'
        return result

    def count_on(self):
        return sum([sum(self._screen[r]) for r in self.rows()])

    def rect(self, width, height):
        for r in range(height):
            for c in range(width):
                self._screen[r][c] = 1

    def rotate_column(self, column, rotate):
        for _ in range(rotate):
            last_val = self._screen[-1][column]
            for r in range(len(self._screen) - 1, 0, -1):
                self._screen[r][column] = self._screen[r-1][column]
            self._screen[0][column] = last_val

    def rotate_row(self, row, rotate):
        for _ in range(rotate):
            last_val = self._screen[row][-1]
            for c in range(len(self._screen[row]) - 1, 0, -1):
                self._screen[row][c] = self._screen[row][c-1]
            self._screen[row][0] = last_val


def read_data(filename):
    with open(filename, 'rt') as file:
        data = [line.strip() for line in file]
    return data


if __name__ == '__main__':
    data = read_data('input.txt')
    screen = Screen(50, 6)
    for line in data:
        terms = line.split(' ')
        if terms[0] == 'rect':
            w, h = terms[1].split('x')
            screen.rect(int(w), int(h))
        if terms[0] == 'rotate':
            rotate = int(terms[4])
            idx = int(terms[2].split('=')[1])
            if terms[1] == 'row':
                screen.rotate_row(idx, rotate)
            if terms[1] == 'column':
                screen.rotate_column(idx, rotate)
    print('Part One: {0}'.format(screen.count_on()))
    print('Part Two:')
    for s in screen.show():
        print(s)
