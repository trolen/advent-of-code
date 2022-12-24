def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class Application:
    def __init__(self, raw_input):
        self._grid = [[int(ch) for ch in line] for line in raw_input]
        self._num_rows = len(self._grid)
        self._num_cols = len(self._grid[0])

    def _edge(self, r, c):
        return r == 0 or c == 0 or r == self._num_rows - 1 or c == self._num_cols - 1

    def _take_step(self, r, c, direction):
        return r + direction[0], c + direction[1]

    def _in_grid(self, r, c):
        return 0 <= r < self._num_rows and 0 <= c < self._num_cols

    def do_part1(self):
        n_visible = 0
        for r in range(self._num_rows):
            for c in range(self._num_cols):
                if self._edge(r, c):
                    n_visible += 1
                    continue
                n = self._grid[r][c]
                r_dirs = (-1, 1) if r < self._num_rows / 2 else (1, -1)
                c_dirs = (-1, 1) if c < self._num_cols / 2 else (1, -1)
                directions = [(r_dirs[0], 0), (0, c_dirs[0]), (r_dirs[1], 0), (0, c_dirs[1])]
                for direction in directions:
                    (r1, c1) = self._take_step(r, c, direction)
                    is_visible = True
                    while self._in_grid(r1, c1):
                        if self._grid[r1][c1] >= n:
                            is_visible = False
                            break
                        (r1, c1) = self._take_step(r1, c1, direction)
                    if is_visible:
                        n_visible += 1
                        break
        return n_visible

    def do_part2(self):
        max_score = 0
        for r in range(self._num_rows):
            for c in range(self._num_cols):
                n = self._grid[r][c]
                score = 1
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for direction in directions:
                    (r1, c1) = self._take_step(r, c, direction)
                    cnt = 0
                    while self._in_grid(r1, c1):
                        cnt += 1
                        if self._grid[r1][c1] >= n:
                            break
                        (r1, c1) = self._take_step(r1, c1, direction)
                    score *= cnt
                    if score == 0:
                        break
                max_score = max(max_score, score)
        return max_score


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
