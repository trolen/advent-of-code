
def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._data = [[int(x) for x in line.split(' ')] for line in raw_input]

    def _find_next(self, numbers):
        if all(n == 0 for n in numbers):
            return 0
        differences = [(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers))]
        return numbers[-1] + self._find_next(differences)

    def do_part1(self):
        return sum(self._find_next(row) for row in self._data)

    def do_part2(self):
        return sum(self._find_next(row[::-1]) for row in self._data)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
