#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        self._instructions = []
        for line in raw_data:
            items = line.split(' = ')
            left_value = items[0]
            right_value = items[1]
            if left_value == 'mask':
                self._instructions.append((left_value, right_value))
                continue
            if not left_value[:3] == 'mem':
                print('Error parsing input')
                exit(1)
            l = len(left_value)
            loc = int(left_value[4:l-1])
            self._instructions.append(('mem', int(loc), int(right_value)))

    def do_part1(self):
        mask = 'X'*36
        memory = {}
        for inst in self._instructions:
            if inst[0] == 'mask':
                mask = inst[1]
                continue
            loc = inst[1]
            value = inst[2]
            for shift in range(0, 36):
                i = 35 - shift
                if mask[i] == 'X':
                    continue
                if mask[i] == '1':
                    value |= (1 << shift)
                elif mask[i] == '0':
                    value &= ~(1 << shift)
            memory[loc] = value
        return sum(memory.values())

    def do_part2(self):
        mask = '0'*36
        memory = {}
        cnt = 0
        for inst in self._instructions:
            cnt += 1
            if inst[0] == 'mask':
                mask = inst[1]
                continue
            locations = [inst[1]]
            value = inst[2]
            for shift in range(0, 36):
                i = 35 - shift
                if mask[i] == '0':
                    continue
                new_locations = []
                for j in range(0, len(locations)):
                    locations[j] |= (1 << shift)
                    if mask[i] == 'X':
                        new_locations.append(locations[j] & ~(1 << shift))
                for new_loc in new_locations:
                    locations.append(new_loc)
            for loc in locations:
                memory[loc] = value
        return sum(memory.values())

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
