def read_input(filename):
    with open(filename) as file:
        return [line.strip('\n') for line in file.readlines()]


class Application:
    def __init__(self):
        self._directions = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    def _parse_input(self, raw_input):
        self._motions = []
        for line in raw_input:
            [direction, steps] = line.split(' ')
            self._motions.append({'direction': direction, 'steps': int(steps)})

    def _simulate(self, snake_length):
        snake = [(0, 0) for i in range(snake_length)]
        points_visited = [snake[-1]]
        for move in self._motions:
            dx, dy = self._directions[move['direction']]
            steps = move['steps']
            while steps > 0:
                snake[0] = (snake[0][0] + dx, snake[0][1] + dy)
                n = 1
                while n < snake_length:
                    dx1 = snake[n - 1][0] - snake[n][0]
                    dy1 = snake[n - 1][1] - snake[n][1]
                    inc_x = inc_y = 0
                    abs_dx1 = abs_dy1 = 0
                    if dx1 != 0:
                        abs_dx1 = abs(dx1)
                        inc_x = dx1 / abs_dx1
                    if dy1 != 0:
                        abs_dy1 = abs(dy1)
                        inc_y = dy1 / abs_dy1
                    if abs_dx1 > 1 or abs_dy1 > 1:
                        snake[n] = (snake[n][0] + inc_x, snake[n][1] + inc_y)
                    n += 1
                if snake[-1] not in points_visited:
                    points_visited.append(snake[-1])
                steps -= 1
        return len(points_visited)

    def do_part1(self, raw_input):
        self._parse_input(raw_input)
        return self._simulate(2)

    def do_part2(self, raw_input):
        self._parse_input(raw_input)
        return self._simulate(10)


def main():
    raw_input = read_input('input.txt')
    app = Application()
    print('Part 1:', app.do_part1(raw_input))
    print('Part 2:', app.do_part2(raw_input))


if __name__ == '__main__':
    main()
