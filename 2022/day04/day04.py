def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._pairs = []
        for line in raw_input:
            pair = []
            terms = line.split(',')
            for term in terms:
                [n1, n2] = [int(s) for s in term.split('-')]
                pair.append([x for x in range(n1, n2 + 1)])
            self._pairs.append(pair)

    def do_part1(self):
        cnt = 0
        for [e1, e2] in self._pairs:
            if e1[0] <= e2[0] and e2[-1] <= e1[-1]:
                cnt += 1
            elif e2[0] <= e1[0] and e1[-1] <= e2[-1]:
                cnt += 1
        return cnt

    def do_part2(self):
        cnt = 0
        for [e1, e2] in self._pairs:
            if e1[0] <= e2[0] <= e1[-1]:
                cnt += 1
            elif e1[0] <= e2[-1] <= e1[-1]:
                cnt += 1
            elif e2[0] <= e1[0] <= e2[-1]:
                cnt += 1
            elif e2[0] <= e1[-1] <= e2[-1]:
                cnt += 1
        return cnt


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
