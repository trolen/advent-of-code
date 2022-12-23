def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Path:
    def __init__(self, parent):
        self.parent = parent
        self.size = 0
        self.directories = []
        self.files = []


def join_paths(p1, p2):
    if p1[-1] == '/':
        return p1 + p2
    return p1 + '/' + p2


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)
        self._calc_size()

    def _cd(self, to):
        if to == '..':
            self._cd(self._paths[self._cwd].parent)
            return
        path = to if to[0] == '/' else join_paths(self._cwd, to)
        if path not in self._paths:
            self._paths[path] = Path(self._cwd)
        self._cwd = path

    def _parse_input(self, raw_input):
        self._cwd = '/'
        self._paths = {}
        for line in raw_input:
            terms = line.split(' ')
            if terms[0] == '$':
                if terms[1] == 'cd':
                    self._cd(terms[2])
            elif terms[0] == 'dir':
                self._paths[self._cwd].directories.append(join_paths(self._cwd, terms[1]))
            elif terms[0].isnumeric():
                self._paths[self._cwd].files.append(File(terms[1], int(terms[0])))

    def _calc_size(self, key='/'):
        directory = self._paths[key]
        if directory.size > 0:
            return directory.size
        size = 0
        for child_dir in directory.directories:
            size += self._calc_size(child_dir)
        for file in directory.files:
            size += file.size
        directory.size = size
        return size

    def do_part1(self):
        result = 0
        for key in self._paths:
            if self._paths[key].size <= 100000:
                result += self._paths[key].size
        return result

    def do_part2(self):
        total_space = 70000000
        required_free_space = 30000000
        used_space = self._paths['/'].size
        free_space = total_space - used_space
        if free_space >= required_free_space:
            return 0
        space_needed = required_free_space - free_space
        result = total_space
        for key in self._paths:
            if self._paths[key].size >= space_needed:
                result = min(result, self._paths[key].size)
        return result


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
