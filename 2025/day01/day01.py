
def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.rotations = raw_input

    def _follow_rotations(self, count_crossings = False):
        count = 0
        dial = 50
        for item in self.rotations:
            direction = 1 if item[0] == 'R' else -1
            distance = int(item[1:])
            if count_crossings:
                start = dial if direction == 1 else (100 - dial) % 100
                count += (start + distance) // 100
            dial = (dial + direction * distance) % 100
            if not count_crossings and dial == 0:
                count += 1
        return count
    
    def do_part1(self):
        return self._follow_rotations()
    
    def do_part2(self):
        return self._follow_rotations(True)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
