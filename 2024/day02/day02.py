
def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.reports = [[int(x) for x in line.split(' ')] for line in raw_input]

    def is_safe(self, report):
        prev_direction = 0
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            abs_diff = abs(diff)
            if abs_diff < 1 or abs_diff > 3:
                return False
            direction = diff / abs_diff
            if prev_direction == 0:
                prev_direction = direction
            if direction != prev_direction:
                return False
        return True

    def count_safe(self, part2=False):
        result = 0
        for report in self.reports:
            if self.is_safe(report):
                result += 1
                continue
            if not part2:
                continue
            for i in range(len(report)):
                newReport = [report[j] for j in range(i)] + [report[j] for j in range(i + 1, len(report))]
                if (self.is_safe(newReport)):
                    result += 1
                    break
        return result

    def do_part1(self):
        return self.count_safe()

    def do_part2(self):
        return self.count_safe(True)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
