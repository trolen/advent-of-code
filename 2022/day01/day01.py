def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        current_elf = 0
        calories = []
        for line in raw_input:
            stripped = line.strip()
            if len(stripped) == 0:
                current_elf += 1
                continue
            if current_elf >= len(calories):
                calories.append(0)
            calories[current_elf] += int(stripped)
        self._calories = sorted(calories, reverse=True)

    def do_part1(self):
        return self._calories[0]

    def do_part2(self):
        return sum(self._calories[0:3])


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
