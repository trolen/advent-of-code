import re

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.guards = '^>v<'
        self.rawInput = raw_input

    def initGrid(self):
        raw_input = [line for line in self.rawInput]
        self.grid = []
        self.currentPosition = [-1, -1]
        for r in range(len(raw_input)):
            line = raw_input[r]
            newLine = []
            for c in range(len(line)):
                ch = line[c]
                newLine.append(ch)
                if ch in self.guards:
                    self.currentPosition = [r, c]
            self.grid.append(newLine)

    def isInGrid(self, r, c):
        return r >= 0 and r < len(self.grid) and c >= 0 and c < len(self.grid[0])

    def move(self):
        r = self.currentPosition[0]
        c = self.currentPosition[1]
        ch = self.grid[r][c]
        rNext = r
        cNext = c
        if ch == '^':
            rNext = r - 1
            chNext = '>'
        elif ch == '>':
            cNext = c + 1
            chNext = 'v'
        elif ch == 'v':
            rNext = r + 1
            chNext = '<'
        elif ch == '<':
            cNext = c - 1
            chNext = '^'
        if self.isInGrid(rNext, cNext):
            if self.grid[rNext][cNext] == '#':
                self.grid[r][c] = chNext
                return
            self.grid[rNext][cNext] = ch
        self.currentPosition = [rNext, cNext]
        self.grid[r][c] = 'X'

    def do_part1(self):
        self.initGrid()
        while self.isInGrid(self.currentPosition[0], self.currentPosition[1]):
            self.move()
        result = 0
        for row in self.grid:
            result += row.count('X')
        return result

    def do_part2(self):
        return 0


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
