import math
import re
from functools import reduce

def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._startRE = re.compile('..A')
        self._endRE = re.compile('..Z')
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._instructions = raw_input[0]
        self._nodes = {}
        for line in raw_input[2:]:
            self._nodes[line[0:3]] = {'L': line[7:10], 'R': line[12:15]}
    
    def _at_end(self, node, part2=False):
        if not part2:
            return node == 'ZZZ'
        return self._endRE.match(node)

    def _travel_network(self, startNode, part2=False):
        steps = 0
        idx = 0
        currentNode = startNode
        while not self._at_end(currentNode, part2):
            instr = self._instructions[idx]
            node = self._nodes[currentNode]
            currentNode = node[instr]
            steps += 1
            idx += 1
            if idx >= len(self._instructions):
                idx = 0
        return steps

    def do_part1(self):
        return self._travel_network('AAA')

    def do_part2(self):
        steps = []
        for key in self._nodes:
            if self._startRE.match(key):
                steps.append(self._travel_network(key, True))
        result = reduce(lambda x,y: (x*y)//math.gcd(x,y), steps)
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
