
def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.list1 = []
        self.list2 = []
        for line in raw_input:
            terms = line.split('   ')
            self.list1.append(int(terms[0]))
            self.list2.append(int(terms[1]))
        self.list1.sort()
        self.list2.sort()

    def do_part1(self):
        result = 0
        for i in range(len(self.list1)):
            result += abs(self.list1[i] - self.list2[i])
        return result

    def do_part2(self):
        result = 0
        for i in range(len(self.list1)):
            cnt = self.list2.count(self.list1[i])
            result += self.list1[i] * cnt
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
