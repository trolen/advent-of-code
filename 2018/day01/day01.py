#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [int(x.strip()) for x in file.readlines()]


def calc_changes_impl(data, frequencies):
    repeated_value = None
    for i in data:
        value = frequencies[-1] + i
        if repeated_value is None and value in frequencies:
            repeated_value = value
        frequencies.append(value)
    return repeated_value


def calc_frequecy_changes(data, part2=False):
    frequencies = [0]
    repeated_value = calc_changes_impl(data, frequencies)
    final_value = frequencies[-1]
    if part2:
        while repeated_value is None:
            repeated_value = calc_changes_impl(data, frequencies)
        return repeated_value
    return final_value


if __name__ == '__main__':
    data = read_data('input.txt')
    final_value = calc_frequecy_changes(data)
    print('Final result: {0}'.format(final_value))
    repeated_value = calc_frequecy_changes(data, part2=True)
    print('Repeated value: {0}'.format(repeated_value))