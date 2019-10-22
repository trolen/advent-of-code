#! /usr/bin/env python3

from datetime import datetime

class Step:
    def __init__(self, timer):
        self._requisites = []
        self._done = False
        self._started = False
        self._timer = timer

    def add_requisite(self, req):
        self._requisites.append(req)

    def remove_requisite(self, req):
        if req in self._requisites:
            self._requisites.remove(req)

    def is_ready(self):
        return not self._started and len(self._requisites) == 0

    def is_done(self):
        return self._done

    def perform(self):
        self._started = True
        if self._timer is not None and self._timer > 0:
            self._timer -= 1
        if self._timer is None or self._timer == 0:
            self._done = True


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


def calc_timer(offset, step):
    return None if offset is None else offset + 1 + ord(step) - ord('A')


def parse_steps(data, offset=None):
    results = {}
    for line in data:
        terms = line.split(' ')
        step1 = terms[1]
        timer1 = calc_timer(offset, step1)
        step2 = terms[7]
        timer2 = calc_timer(offset, step2)
        if step1 not in results:
            results[step1] = Step(timer1)
        if step2 not in results:
            results[step2] = Step(timer2)
        results[step2].add_requisite(step1)
    return results


def all_finished(steps):
    for key in steps:
        if not steps[key].is_done():
            return False
    return True


def perform_step(todo, steps):
    steps[todo].perform()
    if steps[todo].is_done():
        for key in steps:
            steps[key].remove_requisite(todo)


def determine_order(data, num_workers=1, offset=None):
    results = ''
    steps = parse_steps(data, offset)
    keys = sorted(steps.keys())
    workers = ['.'] * num_workers
    time_to_finish = 0
    while not all_finished(steps):
        for key in keys:
            if steps[key].is_ready():
                for i in range(0, len(workers)):
                    if workers[i] == '.':
                        workers[i] = key
                        break
        for i in range(0, len(workers)):
            step = workers[i]
            if step != '.':
                perform_step(step, steps)
                if steps[step].is_done():
                    workers[i] = '.'
                    results += step
        time_to_finish += 1
    return (results, time_to_finish)


if __name__ == '__main__':
    data = read_data('input.txt')
    (s, t) = determine_order(data)
    print('Step order (1 worker): {0}'.format(s))
    (s, t) = determine_order(data, num_workers=5, offset=60)
    print('Step order (5 workers): {0}'.format(s))
    print('Time to Finish: {0} sec'.format(t))