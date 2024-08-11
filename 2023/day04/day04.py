import re

def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        lines = [line.strip() for line in raw_input]
        self._parse_input(lines)

    def _parse_input(self, lines):
        point_total = 0
        copies = [1] * len(lines)
        for i in range(len(lines)):
            line = lines[i]
            a = line.index(':')
            items = [re.sub(' +', ' ', x.strip()) for x in line[a+1:].split('|')]
            winners = [int(x) for x in items[0].split()]
            numbers = [int(x) for x in items[1].split()]
            cnt = 0
            for number in numbers:
                if number in winners:
                    cnt += 1
            if cnt > 0:
                point_total += 2 ** (cnt - 1)
            for j in range(cnt):
                k = i + j + 1
                if k < len(copies):
                    copies[k] += copies[i]
        self._point_total = point_total
        self._copies = sum(copies)

    def do_part1(self):
        return self._point_total

    def do_part2(self):
        return self._copies


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
