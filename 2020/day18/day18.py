#! /usr/bin/env python3

class Application:
    def __init__(self, raw_data):
        self._data = self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        result = []
        for line in raw_data:
            expression = []
            term = ''
            for i in range(0, len(line)):
                ch = line[i]
                if ch == ' ':
                    continue
                if ch.isdigit():
                    term += ch
                    continue
                if len(term) > 0:
                    expression.append(term)
                    term = ''
                expression.append(ch)
            if len(term) > 0:
                expression.append(term)
            result.append(expression)
        return result

    def _do_operation(self, term1, operator, term2):
        if operator == '+':
            return term1 + term2
        if operator == '*':
            return term1 * term2
        return None

    def _evaluate_expression(self, expression, method=1):
        paren_level = 0
        sub_expr = []
        new_expression = []
        for element in expression:
            if element == '(':
                paren_level += 1
                if paren_level == 1:
                    continue
            if element == ')':
                paren_level -= 1
                if paren_level == 0:
                    elem = self._evaluate_expression(sub_expr, method)
                    sub_expr = []
                    new_expression.append(str(elem))
                    continue
            if paren_level > 0:
                sub_expr.append(element)
                continue
            new_expression.append(element)
        expression = new_expression
        if method == 2:
            new_expression = []
            for element in expression:
                if element.isdigit() and len(new_expression) > 0:
                    if new_expression[-1] == '+':
                        new_expression.pop(-1)
                        n1 = int(new_expression.pop(-1))
                        n2 = int(element)
                        new_expression.append(str(self._do_operation(n1, '+', n2)))
                        continue
                new_expression.append(element)
            expression = new_expression
        result = 0
        operator = '+'
        for element in expression:
            if element.isdigit():
                n = int(element)
                result = self._do_operation(result, operator, n)
                continue
            operator = element
        return result

    def do_part1(self):
        result = 0
        for expr in self._data:
            result += self._evaluate_expression(expr)
        return result

    def do_part2(self):
        result = 0
        for expr in self._data:
            result += self._evaluate_expression(expr, 2)
        return result

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 1 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
