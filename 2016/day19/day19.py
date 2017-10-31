#! /usr/bin/env python3

class ElfCircle:
    def __init__(self, num_elves):
        self._elves = []
        for elf in range(1, num_elves + 1):
            self._elves.append((elf, 1))

    def _next_elf(self, idx):
        return (idx + 1) % len(self._elves)

    def _across_from(self, idx):
        n_elves = len(self._elves)
        return (idx + (n_elves // 2)) % n_elves

    def _steal_gifts(self, idx, steal_across=False):
        if steal_across:
            steal_idx = self._across_from(idx)
        else:
            steal_idx = self._next_elf(idx)
        cur_elf, value = self._elves[idx]
        value += self._elves[steal_idx][1]
        self._elves[idx] = (cur_elf, value)
        del self._elves[steal_idx]
        return idx - 1 if steal_idx < idx else idx


    def play_game(self, steal_across=False):
        idx = -1
        n_elves = len(self._elves)
        while n_elves > 1:
            idx = self._steal_gifts((idx + 1) % n_elves, steal_across)
            n_elves = len(self._elves)
        return self._elves[0][0]


if __name__ == '__main__':
    num_elves = 3005290
    elf_circle = ElfCircle(num_elves)
    print('Part One: {0}'.format(elf_circle.play_game()))
    elf_circle = ElfCircle(num_elves)
    print('Part Two: {0}'.format(elf_circle.play_game(True)))
