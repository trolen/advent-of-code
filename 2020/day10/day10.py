#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self.numbers = self.parse_data(raw_data)

    def parse_data(self, raw_data):
        sorted_numbers = sorted([int(line) for line in raw_data])
        return [0] + sorted_numbers + [sorted_numbers[-1] + 3]

    def find_differences(self):
        l = len(self.numbers)
        return [self.numbers[i] - self.numbers[i-1] for i in range(1, l)]

    def do_part1(self):
        differences = self.find_differences()
        n1 = differences.count(1)
        n3 = differences.count(3)
        return n1 * n3

    def build_diff_data(self):
        self.diff_data = {}
        l = len(self.numbers)
        for i in range(0, l - 1):
            data = []
            for j in range(i + 1, l):
                diff = self.numbers[j] - self.numbers[i]
                if diff > 3:
                    break
                data.append(j)
            self.diff_data[self.numbers[i]] = {'result': 0, 'data': data}

    def find_num_arrangements(self, start):
        result = self.diff_data[start]['result']
        if result > 0:
            return result
        nums = self.diff_data[start]['data']
        for n in nums:
            if self.numbers[n] not in self.diff_data:
                result += 1
            else:
                result += self.find_num_arrangements(self.numbers[n])
        self.diff_data[start]['result'] = result
        return result

    def do_part2(self):
        self.build_diff_data()
        return self.find_num_arrangements(0)

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
