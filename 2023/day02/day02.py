def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    _bag_contents = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }


    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        total_possible = 0
        total_power = 0
        for i in range(len(raw_input)):
            line = raw_input[i].strip()
            items = line.split(':')
            cube_sets = items[1].split(';')
            is_possible = True
            minimum_bag = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
            for cube_set in cube_sets:
                cubes = cube_set.split(',')
                for cube in cubes:
                    [number, color] = cube.strip().split(' ')
                    number = int(number)
                    if number > self._bag_contents[color]:
                        is_possible = False
                    if number > minimum_bag[color]:
                        minimum_bag[color] = number
            if is_possible:
                total_possible += i + 1
            total_power += minimum_bag['red'] * minimum_bag['green'] * minimum_bag['blue']
        self._total_possible = total_possible
        self._total_power = total_power


    def do_part1(self):
        return self._total_possible

    def do_part2(self):
        return self._total_power


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
