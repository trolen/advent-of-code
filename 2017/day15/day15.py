#! /usr/bin/env python3

class Generator:
    def __init__(self, start, factor, mult):
        self._start = start
        self._factor = factor
        self._mult = mult
        self.reset()

    def reset(self):
        self._prev = self._start

    def _next_value(self):
        return (self._prev * self._factor) % 2147483647

    def _is_multiple(self):
        result = self._prev % self._mult
        return result == 0

    def next(self, use_mult=False):
        self._prev = self._next_value()
        while use_mult and not self._is_multiple():
            self._prev = self._next_value()
        return self._prev


class GeneratorA(Generator):
    def __init__(self, start):
        super().__init__(start, 16807, 4)


class GeneratorB(Generator):
    def __init__(self, start):
        super().__init__(start, 48271, 8)


def compare_generators(gen_a, gen_b, num_compares, use_mult=False):
    result = 0
    for _ in range(num_compares):
        a_value = gen_a.next(use_mult) & 65535
        b_value = gen_b.next(use_mult) & 65535
        if a_value == b_value:
            result += 1
    return result


if __name__ == '__main__':
    gen_a = GeneratorA(883)
    gen_b = GeneratorB(879)
    print('Part One: {0}'.format(compare_generators(gen_a, gen_b, 40000000)))
    gen_a.reset()
    gen_b.reset()
    print('Part Two: {0}'.format(compare_generators(gen_a, gen_b, 5000000, use_mult=True)))
