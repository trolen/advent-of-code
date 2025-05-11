import re

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._input = []
        enabled = True
        for line in raw_input:
            isEnabled = []
            for i in range(len(line)):
                if line[i:].startswith('don\'t'):
                    enabled = False
                elif line[i:].startswith('do'):
                    enabled = True
                isEnabled.append(enabled)
            for m in re.finditer(r'mul\((\d+),(\d+)\)', line):
                self._input.append([isEnabled[m.start()], int(m.group(1)) * int(m.group(2))])

    def do_part1(self):
        return sum(i[1] for i in self._input)

    def do_part2(self):
        return sum([i[1] if i[0] else 0 for i in self._input])


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
