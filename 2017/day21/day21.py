#! /usr/bin/env python3

class Rule:
    def __init__(self, text):
        self._text = text
        self._parse_rule()

    def _parse_rule(self):
        pattern_text, output_text = (term.strip() for term in self._text.split('=>'))
        pattern = self._parse_pattern(pattern_text)
        self._size = len(pattern)
        self._patterns = []
        for _ in range(4):
            self._append_pattern(pattern)
            self._append_pattern(self._flip(pattern))
            pattern = self._rotate(pattern)
        self._output = self._parse_pattern(output_text)

    def _parse_pattern(self, text):
        return [[ch for ch in row] for row in text.split('/')]

    def _flip(self, pattern):
        result = []
        for row in pattern:
            result.append(row[::-1])
        return result

    def _rotate(self, pattern):
        result = []
        for col in range(self._size):
            result.append([row[col] for row in pattern[::-1]])
        return result

    def _append_pattern(self, pattern):
        if pattern not in self._patterns:
            self._patterns.append(pattern)

    def equal(self, pattern):
        if self._size != len(pattern):
            return False
        for p in self._patterns:
            result = True
            for i in range(self._size):
                if p[i] != pattern[i]:
                    result = False
            if result:
                return True
        return False

    def output(self):
        return self._output


class Program:
    def __init__(self, data):
        self._data = data
        self._rules = [Rule(line) for line in data]

    def _initialize_grid(self):
        self._grid = [
            ['.','#','.'],
            ['.','.','#'],
            ['#','#','#']
        ]

    def _get_div(self, iDiv, jDiv, div_size):
        row = iDiv * div_size
        col = jDiv * div_size
        div = []
        for i in range(div_size):
            div.append(self._grid[row + i][col : col+div_size])
        return div

    def _get_output(self, div):
        for rule in self._rules:
            if rule.equal(div):
                return rule.output()
        return None

    def _run_once(self):
        grid_size = len(self._grid)
        div_size = 2 if (grid_size % 2) == 0 else 3
        num_divs = grid_size // div_size
        output_size = div_size + 1
        new_grid = []
        for iDiv in range(num_divs):
            for _ in range(output_size):
                new_grid.append([])
            for jDiv in range(num_divs):
                div = self._get_div(iDiv, jDiv, div_size)
                output = self._get_output(div)
                for i in range(output_size):
                    new_grid[(iDiv * output_size) + i] += output[i]
        self._grid = new_grid

    def run(self, num):
        self._initialize_grid()
        for i in range(num):
            print('\r{0:02.2f} %'.format(100 * i / num), end='')
            self._run_once()
        print('\r100 %')
        return sum(row.count('#') for row in self._grid)


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    prog = Program(data)
    print('Part One: {0}'.format(prog.run(5)))
    print('Part Two: {0}'.format(prog.run(18)))
