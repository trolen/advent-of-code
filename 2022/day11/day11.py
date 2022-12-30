def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Item:
    def __init__(self, value, is_part1=True):
        self._value = value
        self._is_part1 = is_part1
        self._divisible_by = {i: value % i for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]}

    def update_on_add(self, add_value):
        if self._is_part1:
            self._value = (self._value + add_value) // 3
            return
        for key, value in self._divisible_by.items():
            self._divisible_by[key] = (value + add_value) % key

    def update_on_multiply(self, multiply_value):
        if self._is_part1:
            self._value = (self._value * multiply_value) // 3
            return
        for key, value in self._divisible_by.items():
            self._divisible_by[key] = (value * multiply_value) % key

    def update_on_square(self):
        if self._is_part1:
            self._value = (self._value * self._value) // 3
            return
        for key, value in self._divisible_by.items():
            self._divisible_by[key] = (value * value) % key

    def divisible_by(self, key):
        if self._is_part1:
            return self._value % key
        return self._divisible_by[key]


class Monkey:
    def __init__(self, items: list[Item], operation: str, arg: str, divisible_by: int, throw_to: list[int]):
        self.items = items
        self.operation = operation
        self.arg = arg
        self.divisible_by = divisible_by
        self.throw_to = throw_to
        self.inspections = 0

    def update_items(self):
        if self.operation == '+':
            for item in self.items:
                item.update_on_add(int(self.arg))
        elif self.arg == 'old':
            for item in self.items:
                item.update_on_square()
        else:
            for item in self.items:
                item.update_on_multiply(int(self.arg))
        self.inspections += len(self.items)

    def get_monkeys_to_send(self):
        send_on_true = [item for item in self.items if item.divisible_by(self.divisible_by) == 0]
        send_on_false = [item for item in self.items if item.divisible_by(self.divisible_by) != 0]
        self.items = []
        return {self.throw_to[0]: send_on_true, self.throw_to[1]: send_on_false}

    def receive_items(self, items_to_receive: list[Item]):
        self.items.extend(items_to_receive)


class Application:
    def __init__(self):
        self._monkeys = []

    def _parse_input(self, raw_input, is_part1=True):
        monkeys = []
        items, throw_to = [], []
        divisible_by = 0
        operation, arg = '', ''
        for line in raw_input:
            if line.startswith('Starting'):
                terms = line.split(': ')
                items = [Item(int(item), is_part1) for item in terms[1].split(', ')]
            elif line.startswith('Operation'):
                terms = line.split(' ')
                operation = terms[-2]
                arg = terms[-1]
            elif line.startswith('Test'):
                terms = line.split(' ')
                divisible_by = int(terms[-1])
            elif line.startswith('If true'):
                terms = line.split(' ')
                throw_to = [int(terms[-1])]
            elif line.startswith('If false'):
                terms = line.split(' ')
                throw_to.append(int(terms[-1]))
                monkeys.append(Monkey(items, operation, arg, divisible_by, throw_to))
        self._monkeys = monkeys

    def _do_single_round(self):
        for monkey in self._monkeys:
            monkey.update_items()
            monkeys_to_send = monkey.get_monkeys_to_send()
            for key in monkeys_to_send.keys():
                self._monkeys[key].receive_items(monkeys_to_send[key])

    def _do_rounds(self, n):
        for i in range(n):
            self._do_single_round()
        sorted_inspection_counts = sorted([m.inspections for m in self._monkeys], reverse=True)
        return sorted_inspection_counts[0] * sorted_inspection_counts[1]

    def do_part1(self, raw_input):
        self._parse_input(raw_input)
        return self._do_rounds(20)

    def do_part2(self, raw_input):
        self._parse_input(raw_input, is_part1=False)
        return self._do_rounds(10000)


def main():
    raw_input = read_input('input.txt')
    app = Application()
    print('Part 1:', app.do_part1(raw_input))
    print('Part 2:', app.do_part2(raw_input))


if __name__ == '__main__':
    main()
