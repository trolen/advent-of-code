def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._raw_input = raw_input

    def _parse_input(self, raw_input):
        stacks_input = []
        stacks_finished = False
        self._stacks = {}
        self._moves = []
        for line in raw_input:
            if len(line) == 0:
                stacks_finished = True
                continue
            if not stacks_finished:
                stacks_input.append(line)
                continue
            terms = line.split(' ')
            self._moves.append({'move': int(terms[1]), 'from': terms[3], 'to': terms[5]})
        for line in reversed(stacks_input):
            if line[1].isdigit():
                for x in line:
                    if x.isdigit():
                        self._stacks[x] = []
                continue
            n = 1
            while n < len(line):
                c = line[n]
                if c.isalpha():
                    key = str((n - 1)//4 + 1)
                    self._stacks[key].append(c)
                n += 4

    def do_part1(self):
        self._parse_input(self._raw_input)
        for move in self._moves:
            for i in range(move['move']):
                crate = self._stacks[move['from']].pop()
                self._stacks[move['to']].append(crate)
        result = ''
        for key in self._stacks.keys():
            result += self._stacks[key][-1]
        return result

    def do_part2(self):
        self._parse_input(self._raw_input)
        for move in self._moves:
            i = move['move']
            while i > 0:
                crate = self._stacks[move['from']].pop(-i)
                self._stacks[move['to']].append(crate)
                i -= 1
        result = ''
        for key in self._stacks.keys():
            result += self._stacks[key][-1]
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
