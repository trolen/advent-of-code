#! /usr/bin/env python3


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None


class Cups:
    def __init__(self):
        self._nodes_map = {}
        self.head = None
        self.tail = None
        self.min = None
        self.max = None

    def append(self, value):
        self.min = value if self.min is None else min(self.min, value)
        self.max = value if self.max is None else max(self.max, value)
        cup = Cup(value)
        self._nodes_map[value] = cup
        if self.head is None:
            self.head = cup
        cup.next = self.head
        if self.tail is not None:
            self.tail.next = cup
        self.tail = cup

    def _pickup(self):
        self._picked_up = []
        for i in range(0, 3):
            cup = self.head.next
            self.head.next = cup.next
            cup.next = None
            self._picked_up.append(cup)

    def _normalize_value(self, value):
        if value < self.min:
            return self.max
        return value

    def _is_picked_up(self, value):
        for cup in self._picked_up:
            if cup.value == value:
                return True
        return False

    def _find(self, value):
        return self._nodes_map[value]

    def _find_destination(self):
        dest_value = self._normalize_value(self.head.value - 1)
        while self._is_picked_up(dest_value):
            dest_value = self._normalize_value(dest_value - 1)
        return self._find(dest_value)

    def move_cups(self):
        self._pickup()
        dest = self._find_destination()
        for cup in self._picked_up[::-1]:
            cup.next = dest.next
            dest.next = cup
        self.tail = self.head
        self.head = self.head.next

    def get_part1_result(self):
        cup = self._find(1)
        result = ''
        while True:
            cup = cup.next
            if cup.value == 1:
                break
            result += str(cup.value)
        return result

    def get_part2_result(self):
        cup = self._find(1)
        result = 1
        for i in range(0, 2):
            cup = cup.next
            result *= cup.value
        return result


class Application:
    def __init__(self, raw_data):
        self._raw_data = raw_data
        self._parse_data()

    def _parse_data(self):
        self._cups = Cups()
        for ch in self._raw_data[0]:
            self._cups.append(int(ch))

    def do_part1(self):
        for i in range(0, 100):
            self._cups.move_cups()
        return self._cups.get_part1_result()

    def _reset_for_part2(self):
        self._parse_data()
        for i in range(self._cups.max + 1, 1000001):
            self._cups.append(i)

    def do_part2(self):
        self._reset_for_part2()
        for i in range(0, 10000000):
            self._cups.move_cups()
        return self._cups.get_part2_result()

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
