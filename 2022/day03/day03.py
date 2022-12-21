def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._rucksacks = [line.strip() for line in raw_input]

    def _calc_score(self, ch):
        score = ord(ch) - ord('a') + 1
        if ch.isupper():
            score = ord(ch) - ord('A') + 27
        return score

    def do_part1(self):
        total = 0
        for sack in self._rucksacks:
            n = len(sack) // 2
            s1 = sack[0:n]
            s2 = sack[n:]
            for ch in s1:
                if ch in s2:
                    total += self._calc_score(ch)
                    break
        return total

    def do_part2(self):
        total = 0
        n_groups = len(self._rucksacks) // 3
        for group in range(n_groups):
            n = group * 3
            s1 = self._rucksacks[n]
            s2 = self._rucksacks[n + 1]
            s3 = self._rucksacks[n + 2]
            for ch in s1:
                if ch in s2 and ch in s3:
                    total += self._calc_score(ch)
                    break
        return total


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
