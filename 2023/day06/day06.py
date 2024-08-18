import re

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._raw_input = raw_input

    def _parse_input(self, lines, part2=False):
        times = lines[0]
        distances = lines[1]
        if part2:
            times = lines[0].replace(' ', '')
            distances = lines[1].replace(' ', '')
        self._times = [int(x) for x in re.findall(r'\d+', times)]
        self._distances = [int(x) for x in re.findall(r'\d+', distances)]

    def _get_possible_wins(self, t, d):
        cnt = 0
        for i in range(1, t):
            r = i * (t - i)
            if (r > d):
                cnt += 1
        return cnt

    def do_part1(self):
        self._parse_input(self._raw_input)
        result = 1
        for i in range(len(self._times)):
            result *= self._get_possible_wins(self._times[i], self._distances[i])
        return result

    def do_part2(self):
        self._parse_input(self._raw_input, True)
        return self._get_possible_wins(self._times[0], self._distances[0])


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
