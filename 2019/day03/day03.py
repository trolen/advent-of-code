#! /usr/bin/env python3

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def parse_wires(raw_data):
    result = []
    for path in raw_data:
        x = 0
        y = 0
        moves = path.split(',')
        wire = []
        for move in moves:
            ch = move[0]
            distance = int(move[1:])
            for i in range(distance):
                if ch == 'R':
                    x += 1
                elif ch == 'L':
                    x -= 1
                elif ch == 'U':
                    y += 1
                elif ch == 'D':
                    y -= 1
                wire.append((x, y))
        result.append(wire)
    return result


def find_crossings(raw_data):
    wires = parse_wires(raw_data)
    wire1 = wires[0]
    wire2 = wires[1]
    result = []
    for i in range(len(wire1)):
        point = wire1[i]
        for j in range(len(wire2)):
            if wire2[j] == point:
                steps = i + j + 2
                result.append((point[0], point[1], steps))
                break
    return result


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def find_closest_crossing(crossings):
    return min(manhattan_distance(p[0], p[1]) for p in crossings)


def find_fewest_steps(crossings):
    return min(p[2] for p in crossings)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    crossings = find_crossings(raw_data)
    distance = find_closest_crossing(crossings)
    print('Closest distance: {0}'.format(distance))
    steps = find_fewest_steps(crossings)
    print('Fewest steps: {0}'.format(steps))
