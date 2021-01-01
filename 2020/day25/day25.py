#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._public_key1 = int(raw_data[0])
        self._public_key2 = int(raw_data[1])

    def _transform(self, value, subject_number):
        return (value * subject_number) % 20201227

    def _find_loop_size(self, subject_number, public_key):
        value = 1
        loop_size = 0
        while value != public_key:
            value = self._transform(value, subject_number)
            loop_size += 1
        return loop_size

    def _calc_encryption_key(self, subject_number, loop_size):
        value = 1
        for i in range(0, loop_size):
            value = self._transform(value, subject_number)
        return value

    def do_part1(self):
        loop_size1 = self._find_loop_size(7, self._public_key1)
        loop_size2 = self._find_loop_size(7, self._public_key2)
        encryption_key1 = self._calc_encryption_key(self._public_key2, loop_size1)
        encryption_key2 = self._calc_encryption_key(self._public_key1, loop_size2)
        if encryption_key1 == encryption_key2:
            return encryption_key1
        return 0

    def do_part2(self):
        return 0

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
