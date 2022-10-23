#! /usr/bin/env python3

import re

from collections import Counter, deque
from itertools import chain, combinations


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


def parse_input(lines):
    return [set(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line)) for line in lines]


def is_valid_floor(floor):
    return len(set(t for _, t in floor)) < 2 or \
           all((obj, 'generator') in floor for (obj, t) in floor if t == 'microchip')


def next_states(state):
    moves, elevator, floors = state
    possible_moves = chain(combinations(floors[elevator], 2), combinations(floors[elevator], 1))
    for move in possible_moves:
        for direction in [-1, 1]:
            next_elevator = elevator + direction
            if not 0 <= next_elevator < len(floors):
                continue
            next_floors = floors.copy()
            next_floors[elevator] = next_floors[elevator].difference(move)
            next_floors[next_elevator] = next_floors[next_elevator].union(move)
            if is_valid_floor(next_floors[elevator]) and is_valid_floor(next_floors[next_elevator]):
                yield moves + 1, next_elevator, next_floors


def is_all_top_level(floors):
    return all(not floor for number, floor in enumerate(floors) if number < len(floors) - 1)


def count_floor_objects(state):
    _, elevator, floors = state
    return elevator, tuple(tuple(Counter(type for _, type in floor).most_common()) for floor in floors)


def min_moves_to_top_level(floors):
    seen = set()
    queue = deque([(0, 0, floors)])
    while queue:
        state = queue.popleft()
        moves, _, floors = state
        if is_all_top_level(floors):
            return moves
        for next_state in next_states(state):
            if (key := count_floor_objects(next_state)) not in seen:
                seen.add(key)
                queue.append(next_state)


def do_part1(data):
    floors = parse_input(data)
    return min_moves_to_top_level(floors)


if __name__ == '__main__':
    rawData = read_data('input.txt')
    result1 = do_part1(rawData)
    print('Part 1 result:', result1)
