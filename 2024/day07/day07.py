def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self.equations = []
        for line in raw_input:
            items = line.split(':')
            result = int(items[0])
            terms = [int(x) for x in items[1].strip().split(' ')]
            self.equations.append([result, terms])

    def calculate(self, terms, operators):
        result = terms[0]
        for i in range(1, len(terms)):
            op = operators[i - 1]
            if op == 0:
                result += terms[i]
            elif op == 1:
                result *= terms[i]
            else:
                result = int(str(result) + str(terms[i]))
        return result

    def incrementOperators(self, operators, base):
        result = [x for x in operators]
        inc = 1
        for i in range(len(result)):
            newValue = result[i] + inc
            result[i] = newValue % base
            inc = newValue // base
        return result

    def canBeTrue(self, index, base):
        equation = self.equations[index]
        result = equation[0]
        terms = equation[1]
        numOperators = len(terms) - 1
        operators = [0 for i in range(numOperators)]
        loopTimes = base ** numOperators
        for i in range(loopTimes):
            value = self.calculate(terms, operators)
            if value == result:
                return True
            operators = self.incrementOperators(operators, base)
        return False

    def do_part1(self):
        result = 0
        for i in range(len(self.equations)):
            if self.canBeTrue(i, 2):
                result += self.equations[i][0]
        return result

    def do_part2(self):
        result = 0
        for i in range(len(self.equations)):
            if self.canBeTrue(i, 3):
                result += self.equations[i][0]
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
