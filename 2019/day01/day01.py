#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [int(x.strip()) for x in file.readlines()]


def fuel_required(mass):
    result = int(mass / 3) - 2
    return result

def fuel_required2(mass):
    fuel = fuel_required(mass)
    result = 0
    while True:
        result += fuel
        fuel = fuel_required(fuel)
        if fuel <= 0:
            return result


if __name__ == '__main__':
    data = read_data('input.txt')
    total_fuel = 0
    for mass in data:
        total_fuel += fuel_required(mass)
    print('Total fuel: {0}'.format(total_fuel))
    total_fuel = 0
    for mass in data:
        total_fuel += fuel_required2(mass)
    print('Total fuel (including extra fuel): {0}'.format(total_fuel))
