#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self.original_grid = raw_data
        self.seat_grid = raw_data

    def reset_grid(self):
        self.seat_grid = self.original_grid

    def count_adjacent_occupied(self, r0, c0, method=1):
        cnt = 0
        for r_step in range(-1, 2):
            for c_step in range(-1, 2):
                if r_step == 0 and c_step == 0:
                    continue
                r = r0
                c = c0
                first_time = True
                while True:
                    if method == 1 and not first_time:
                        break
                    first_time = False
                    r += r_step
                    c += c_step
                    if r < 0 or c < 0:
                        break
                    if r >= len(self.seat_grid) or c >= len(self.seat_grid[r]):
                        break
                    ch = self.seat_grid[r][c]
                    if ch == '#':
                        cnt += 1
                        break
                    if ch == 'L':
                        break
        return cnt

    def model_seat_changes(self, method=1):
        seat_changed = False
        max_occupied = 4 if method == 1 else 5
        new_grid = []
        for i in range(0, len(self.seat_grid)):
            row = self.seat_grid[i]
            new_row = ''
            for j in range(0, len(row)):
                ch = row[j]
                if ch == 'L':
                    if self.count_adjacent_occupied(i, j, method) == 0:
                        ch = '#'
                        seat_changed = True
                elif ch == '#':
                    if self.count_adjacent_occupied(i, j, method) >= max_occupied:
                        ch = 'L'
                        seat_changed = True
                new_row += ch
            new_grid.append(new_row)
        self.seat_grid = new_grid
        return seat_changed

    def count_occupied_seats(self):
        result = 0
        for i in range(0, len(self.seat_grid)):
            result += self.seat_grid[i].count('#')
        return result

    def do_part1(self):
        while self.model_seat_changes():
            pass
        return self.count_occupied_seats()

    def do_part2(self):
        while self.model_seat_changes(method=2):
            pass
        return self.count_occupied_seats()

    def execute(self):
        print('Part 1 result:', self.do_part1())
        self.reset_grid()
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
