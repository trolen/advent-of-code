#! /usr/bin/env python3

class Scrambler:
    def __init__(self, instructions):
        self._instructions = instructions
        self._word = ''

    def _swap(self, x, y):
        i1 = min(x, y)
        i2 = max(x, y)
        c1 = self._word[i1]
        c2 = self._word[i2]
        s1 = self._word[:i1]
        s2 = self._word[i1+1:i2]
        s3 = self._word[i2+1:]
        self._word = s1 + c2 + s2 + c1 + s3

    def _rotate(self, steps):
        l = len(self._word)
        if steps > 0:
            steps = l - (steps % l)
        elif steps < 0:
            steps = -steps
        s = self._word + self._word
        self._word = s[steps:steps+l]

    def _reverse(self, x, y):
        i1 = min(x, y)
        i2 = max(x, y)
        s1 = self._word[:i1]
        s2 = self._word[i1:i2+1]
        s3 = self._word[i2+1:]
        self._word = s1 + s2[::-1] + s3

    def _move(self, x, y):
        c = self._word[x]
        s = self._word[:x] + self._word[x+1:]
        self._word = s[:y] + c + s[y:]

    def _perform_instructions(self, word):
        self._word = word
        for instruction in self._instructions:
            terms = instruction.split()
            if terms[0] == 'swap':
                if terms[1] == 'position':
                    x = int(terms[2])
                    y = int(terms[-1])
                else:
                    x = self._word.find(terms[2])
                    y = self._word.find(terms[-1])
                self._swap(x, y)
                continue
            if terms[0] == 'rotate':
                if terms[1] == 'based':
                    i = self._word.find(terms[-1])
                    steps = i + (2 if i >= 4 else 1)
                else:
                    steps = int(terms[2])
                    if terms[1] == 'left':
                        steps = -steps
                self._rotate(steps)
                continue
            if terms[0] == 'reverse':
                x = int(terms[2])
                y = int(terms[-1])
                self._reverse(x, y)
                continue
            if terms[0] == 'move':
                x = int(terms[2])
                y = int(terms[-1])
                self._move(x, y)
                continue
        return self._word

    def scramble(self, word):
        return self._perform_instructions(word)


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    scrambler = Scrambler(data)
    print('Part One: {0}'.format(scrambler.scramble('abcdefgh')))
    #print('Part Two: {0}'.format(scrambler.unscramble('fbgdceah')))
    #print('Part Two: {0}'.format(scrambler.unscramble('cbeghdaf')))
