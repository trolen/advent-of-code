#! /usr/bin/env python3

KEYPAD1 = [
    '123',
    '456',
    '789'
]

KEYPAD2 = [
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  '
]

def find_five(keypad):
    for row in range(len(keypad)):
        for col in range(len(keypad[row])):
            if keypad[row][col] == '5':
                return (row, col)
    return (0, 0)


def get_code(keypad, input_strings):
    result = ''
    y, x = find_five(keypad)
    for s in input_strings:
        for ch in s:
            y1, x1 = y, x
            if ch == 'L' and x > 0:
                x1 -= 1
            if ch == 'R' and x < len(keypad[y]) - 1:
                x1 += 1
            if ch == 'U' and y > 0:
                y1 -= 1
            if ch == 'D' and y < len(keypad) - 1:
                y1 += 1
            if keypad[y1][x1] != ' ':
                y, x = y1, x1
        result += keypad[y][x]
    return result


if __name__ == '__main__':
    input_strings = []
    with open('input.txt', 'rt') as file:
        for line in file:
            input_strings.append(line.strip())
    print('Part One: {0}'.format(get_code(KEYPAD1, input_strings)))
    print('Part Two: {0}'.format(get_code(KEYPAD2, input_strings)))