#! /usr/bin/env python3

import numpy as np
import time

def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def parse_data(data):
    terms = data.split(' ')
    return (int(terms[0]), int(terms[6]))


def play_game(data, multiplier=1):
    (num_players, last_marble) = parse_data(data)
    last_marble *= multiplier
    marbles = [0]
    scores = [0] * num_players
    cur_position = 0
    marble_to_insert = 1
    while True:
        while marble_to_insert % 23 != 0:
            new_position = (cur_position + 2) % len(marbles)
            marbles.insert(new_position, marble_to_insert)
            cur_position = new_position
            marble_to_insert += 1
        if marble_to_insert > last_marble:
            break
        player = marble_to_insert % num_players
        scores[player] += marble_to_insert
        new_position = cur_position - 7
        if new_position < 0:
            new_position += len(marbles)
        scores[player] += marbles[new_position]
        del marbles[new_position]
        cur_position = new_position % len(marbles)
        marble_to_insert += 1
    return max(scores)


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    start = time.time()
    score = play_game(raw_data)
    end = time.time()
    print('Execution time: {0} sec'.format(end - start))
    print('Score: {0}'.format(score))
    start = time.time()
    score = play_game(raw_data, multiplier=100)
    end = time.time()
    print('Execution time: {0} sec'.format(end - start))
    print('Score: {0}'.format(score))
