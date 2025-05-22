import re

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.grid = [line for line in raw_input]
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])

    def is_word(self, word, r, c, dir):
        row_step = 0
        col_step = 0
        coords = []
        if 'N' in dir:
            if r < len(word) - 1:
                return False
            row_step = -1
        if 'S' in dir:
            if r > self.rows - len(word):
                return False
            row_step = 1
        if 'W' in dir:
            if c < len(word) - 1:
                return False
            col_step = -1
        if 'E' in dir:
            if c > self.columns - len(word):
                return False
            col_step = 1
        for i in range(len(word)):
            r1 = r + i * row_step
            c1 = c + i * col_step
            if self.grid[r1][c1] != word[i]:
                return False
            if word[i] == 'A':
                coords = [r1, c1]
        self.cross_points.append(coords)
        return True

    def find_word(self, word, part2 = False):
        result = 0
        self.cross_points = []
        for r in range(self.rows):
            row = self.grid[r]
            for c in range(self.columns):
                if row[c] != word[0]:
                    continue
                if not part2:
                    if self.is_word(word, r, c, 'N'):
                        result += 1
                    if self.is_word(word, r, c, 'S'):
                        result += 1
                    if self.is_word(word, r, c, 'E'):
                        result += 1
                    if self.is_word(word, r, c, 'W'):
                        result += 1
                if self.is_word(word, r, c, 'NE'):
                    result += 1
                if self.is_word(word, r, c, 'NW'):
                    result += 1
                if self.is_word(word, r, c, 'SE'):
                    result += 1
                if self.is_word(word, r, c, 'SW'):
                    result += 1
        return result

    def do_part1(self):
        return self.find_word('XMAS')

    def do_part2(self):
        self.find_word('MAS', True)
        result = 0
        for i in range(len(self.cross_points)):
            item = self.cross_points[i]
            if self.cross_points.count(item) == 2:
                result += 1
        return int(result / 2)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
