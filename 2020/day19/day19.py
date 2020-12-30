#! /usr/bin/env python3

from parsimonious.grammar import Grammar
from parsimonious import ParseError
import re


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        idx = raw_data.index('')
        self._rules = {}
        for line in raw_data[:idx]:
            rule = int(line.split(':')[0])
            self._rules[rule] = line
        self._messages = raw_data[idx+1:]

    def _convert(self, line):
        line = line.replace(':', ' =')
        line = re.sub(r'(\d+)', r'R\1', line)
        line = re.sub(r'= (.*) \| (.*)$', r'= ((\1) / (\2))', line)
        return line

    def _build_grammar(self):
        sorted_keys = sorted(self._rules.keys())
        sorted_rules = [self._rules[key] for key in sorted_keys]
        converted_rules = '\n'.join([self._convert(r) for r in sorted_rules])
        self._grammar = Grammar(converted_rules)

    def _parse_message(self, message):
        try:
            self._grammar.parse(message)
        except ParseError:
            return False
        return True

    def _parse_messages(self):
        return sum(map(self._parse_message, self._messages))

    def do_part1(self):
        self._build_grammar()
        return self._parse_messages()

    def do_part2(self):
        self._rules[8] = '8: 42 | 42 8'
        self._rules[11] = '11: 42 31 | 42 11 31'
        self._build_grammar()
        return self._parse_messages()

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
