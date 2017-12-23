#! /usr/bin/env python3

from collections import deque

class Spinlock:
    def __init__(self, steps):
        self._steps = steps

    def run(self, max_val, part2=False):
        buffer = deque([0])
        num = max_val + 1
        for i in range(1, num):
            buffer.rotate(-self._steps)
            buffer.append(i)
            print('\r{0:02.2f} %'.format((100 * i) / num), end='')
        print('\r100 %')
        return buffer[0 if not part2 else (buffer.index(0) + 1) % num]

if __name__ == '__main__':
    spinlock = Spinlock(366)
    print('Part One: {0}'.format(spinlock.run(2017)))
    print('Part Two: {0}'.format(spinlock.run(50000000, part2=True)))
