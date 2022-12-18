def read_input(filename):
    with open(filename) as file:
        return file.readlines()


class Application:
    def __init__(self, raw_input):
        self._parse_input(raw_input)

    def _parse_input(self, raw_input):
        self._moves = []
        for line in raw_input:
            self._moves.append(line.strip().split())

    def _score_round(self, opponent, player):
        result = 0
        if player == opponent:
            result = 3
        elif player == (opponent + 1) % 3:
            result = 6
        result += player + 1
        return result

    def do_part1(self):
        score = 0
        for move in self._moves:
            opponent = ord(move[0]) - ord('A')
            player = ord(move[1]) - ord('X')
            score += self._score_round(opponent, player)
        return score

    def do_part2(self):
        score = 0
        for move in self._moves:
            opponent = ord(move[0]) - ord('A')
            result = ord(move[1]) - ord('X')
            player = opponent
            if result == 0:
                player = (opponent + 2) % 3
            elif result == 2:
                player = (opponent + 1) % 3
            score += self._score_round(opponent, player)
        return score


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
