def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._instructions = [line.split(' ') for line in raw_input]

    def _init(self):
        self._register_x = 1
        self._cycle = 1
        self._signal_strengths = []
        self._pixels = []

    def _signal_strength(self):
        return self._cycle * self._register_x

    def _draw_pixel(self):
        row_position = (self._cycle - 1) % 40
        return '#' if abs(self._register_x - row_position) <= 1 else '.'

    def _noop(self):
        self._signal_strengths.append(self._signal_strength())
        self._pixels.append(self._draw_pixel())
        self._cycle += 1

    def _addx(self, arg):
        self._noop()
        self._noop()
        self._register_x += arg

    def _run_operations(self):
        self._init()
        for instruction in self._instructions:
            cmd = instruction[0]
            if cmd == 'noop':
                self._noop()
            elif cmd == 'addx':
                self._addx(int(instruction[1]))

    def do_part1(self):
        self._run_operations()
        return sum(self._signal_strengths[n-1] for n in [20, 60, 100, 140, 180, 220])

    def do_part2(self):
        self._run_operations()
        result = []
        for n in range(6):
            begin = n * 40
            end = begin + 40
            s = ''.join(self._pixels[begin:end])
            result.append(s)
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:')
    for s in app.do_part2():
        print(s)


if __name__ == '__main__':
    main()
