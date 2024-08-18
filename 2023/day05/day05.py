def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Map:
    def __init__(self):
        self._dest = []
        self._source = []
        self._range = []

    def add(self, d, s, r):
        self._dest.append(d)
        self._source.append(s)
        self._range.append(r)

    def find(self, n):
        for i in range(len(self._source)):
            d = self._dest[i]
            s = self._source[i]
            r = self._range[i]
            if n >= s and n < s + r:
                return d + n - s
        return n


class Application:
    def __init__(self, raw_input):
        lines = [line.strip() for line in raw_input]
        self._parse_input(lines)

    def _parse_input(self, lines):
        self._seeds = []
        self._maps = [Map() for i in range(7)]
        map_no = -1
        for line in lines:
            items = line.split(' ')
            if len(items) == 3:
                [d, s, r] = [int(x) for x in items]
                self._maps[map_no].add(d, s, r)
                continue
            if line.startswith('seeds:'):
                self._seeds = [int(s) for s in items[1:]]
                continue
            if len(line) > 0:
                map_no += 1

    def _get_min_location(self, part2=False):
        seeds = []
        lengths = []
        result = -1
        if part2:
            for i in range(0, len(self._seeds), 2):
                seeds.append(self._seeds[i])
                lengths.append(self._seeds[i+1])
        else:
            seeds = self._seeds
            lengths = [1 for x in seeds]
        for i in range(len(seeds)):
            seed = seeds[i]
            length = lengths[i]
            for n in range(seed, seed + length):
                a = n
                for map in self._maps:
                    b = map.find(a)
                    a = b
                result = min(result, a) if result >= 0 else a
        return result

    def do_part1(self):
        return self._get_min_location()

    def do_part2(self):
        return self._get_min_location(True)


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
