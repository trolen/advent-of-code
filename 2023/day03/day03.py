import re

number_re = re.compile('[0-9]+')
symbol_re = re.compile('[^0-9.]')

def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._total_parts = 0
        lines = [line.strip() for line in raw_input]
        self._gears = [[[] for j in range(len(lines[0]))] for i in range(len(lines))]
        self._parse_input(lines)

    def _find_gears(self, s, r, x, part_no):
        for i in range(len(s)):
            if s[i] == '*':
                self._gears[r][x+i].append(part_no)

    def _parse_input(self, lines):
        total_parts = 0
        line_len = len(lines[0])
        for r in range(len(lines)):
            line = lines[r]
            numbers = number_re.findall(line)
            for n in numbers:
                a = line.find(n)
                b = a + len(n)
                x = a - 1 if a > 0 else a
                y = b + 1 if b < line_len else b
                s1 = lines[r - 1][x:y] if r > 0 else ''
                s2 = line[x:y]
                s3 = lines[r + 1][x:y] if r+1 < len(lines) else ''
                test = s1 + s2 + s3
                if not symbol_re.search(test) is None:
                    part_no = int(n)
                    total_parts += part_no
                    self._find_gears(s1, r - 1, x, part_no)
                    self._find_gears(s2, r, x, part_no)
                    self._find_gears(s3, r + 1, x, part_no)
                line = line[:a] + '.'*len(n) + line[b:]
        self._total_parts = total_parts

    def do_part1(self):
        return self._total_parts

    def do_part2(self):
        total_gears = 0
        gears = self._gears
        for i in range(len(gears)):
            for j in range(len(gears[0])):
                if len(gears[i][j]) == 2:
                    x = gears[i][j][0]
                    y = gears[i][j][1]
                    total_gears += x * y
        return total_gears


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
