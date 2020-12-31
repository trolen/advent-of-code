#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_rule(self, line):
        items = line.split(': ')
        rule_no = int(items[0])
        value = items[1]
        if value.startswith('"'):
            self._rules[rule_no] = value[1]
            return
        options = []
        for seq in value.split(' | '):
            rules = []
            for rule in seq.split(' '):
                rules.append(int(rule))
            options.append(rules)
        self._rules[rule_no] = options

    def _parse_data(self, raw_data):
        idx = raw_data.index('')
        rule_lines = raw_data[:idx]
        self._rules = {}
        for line in rule_lines:
            self._parse_rule(line)
        self._messages = raw_data[idx + 1:]

    def _match(self, message, idx, rule):
        if idx >= len(message):
            return []
        value = self._rules[rule]
        if type(value) == str:
            if value == message[idx]:
                return [idx + 1]
            return []
        result = []
        for seq in value:
            try_indexes = [idx]
            for rnum in seq:
                new_indexes = []
                for n in try_indexes:
                    new_indexes += self._match(message, n, rnum)
                try_indexes = new_indexes
            result += try_indexes
        return result

    def _match_messages(self):
        result = 0
        for message in self._messages:
            a = self._match(message, 0, 0)
            for n in a:
                if n == len(message):
                    result += 1
                    break
        return result

    def do_part1(self):
        return self._match_messages()

    def do_part2(self):
        self._parse_rule('8: 42 | 42 8')
        self._parse_rule('11: 42 31 | 42 11 31')
        return self._match_messages()

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
