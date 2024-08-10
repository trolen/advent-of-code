import re

number_re = re.compile('[0-9]+')
symbol_re = re.compile('[^0-9.]')

def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._raw_input = [line.strip() for line in raw_input]
        self._llen = len(raw_input[0])

    def do_part1(self):
        total = 0
        for r in range(len(self._raw_input)):
            line = self._raw_input[r]
            numbers = number_re.findall(line)
            for n in numbers:
                a = line.find(n)
                b = a + len(n)
                x = a - 1 if a > 0 else a
                y = b + 1 if b < self._llen else b
                s1 = self._raw_input[r - 1][x:y] if r > 0 else ''
                s2 = line[x:y]
                s3 = self._raw_input[r + 1][x:y] if r+1 < len(self._raw_input) else ''
                test = s1 + s2 + s3
                if not symbol_re.search(test) is None:
                    total += int(n)
                line = line[:a] + '.'*len(n) + line[b:]
        return total

    #def do_part2(self):
    #    return self._total_power


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    #print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
