#! /usr/bin/env python3

class ElfCircle:
    def __init__(self, num_elves):
        self._elves = [1] * num_elves
        self._num_elves = num_elves

    def _next_elf(self, idx):
        while True:
            idx = (idx + 1) % len(self._elves)
            if self._elves[idx] > 0:
                break
        return idx

    def _across_from(self, idx):
        n_inc = self._num_elves // 2
        for _ in range(n_inc):
            idx = self._next_elf(idx)
        return idx

    def _steal_gifts(self, idx, steal_across=False):
        if steal_across:
            steal_idx = self._across_from(idx)
        else:
            steal_idx = self._next_elf(idx)
        self._elves[idx] += self._elves[steal_idx]
        self._elves[steal_idx] = 0
        self._num_elves -= 1

    def play_game(self, steal_across=False):
        idx = 0
        while True:
            self._steal_gifts(idx, steal_across)
            if self._num_elves == 1:
                break
            idx = self._next_elf(idx)
        return idx + 1


if __name__ == '__main__':
    num_elves = 3005290
    elf_circle = ElfCircle(num_elves)
    print('Part One: {0}'.format(elf_circle.play_game()))
    elf_circle = ElfCircle(num_elves)
    print('Part Two: {0}'.format(elf_circle.play_game(True)))
