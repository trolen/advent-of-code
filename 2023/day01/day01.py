def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._raw_input = raw_input

    def get_calibration(self, part2 = False):
        calibration = 0
        numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for line in self._raw_input:
            stripped = line.strip()
            start = -1
            stop = -1
            for i in range(len(line)):
                ch = line[i]
                value = -1
                if '0' <= ch <= '9':
                    value = ord(ch) - ord('0')
                elif part2:
                    for j in range(len(numbers)):
                        if line[i:].startswith(numbers[j]):
                            value = j + 1
                            break
                if value >= 0:
                    if start < 0:
                        start = value
                    stop = value
            calibration += start * 10 + stop
        return calibration

    def do_part1(self):
        return self.get_calibration()

    def do_part2(self):
        return self.get_calibration(True)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
