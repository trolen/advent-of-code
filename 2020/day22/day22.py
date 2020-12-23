#! /usr/bin/env python3


class CardGame:
    def __init__(self, player1_cards, player2_cards, recursive=False):
        self._player1 = player1_cards
        self._player2 = player2_cards
        self._recursive = recursive
        self._winner = 0
        self._previous_rounds = []

    def _arrays_equal(self, arr1, arr2):
        l1 = len(arr1)
        l2 = len(arr2)
        if l1 != l2:
            return False
        for i in range(0, l1):
            if arr1[i] != arr2[i]:
                return False
        return True

    def _check_state(self):
        for (p1, p2) in self._previous_rounds:
            if self._arrays_equal(self._player1, p1) and self._arrays_equal(self._player2, p2):
                return True
        return False

    def _save_state(self):
        self._previous_rounds.append((self._player1[:],self._player2[:]))

    def _move_card(self, winner, loser):
        winner.append(winner.pop(0))
        winner.append(loser.pop(0))

    def _play_round(self):
        round_winner = 0
        if self._recursive:
            self._save_state()
            card1 = self._player1[0]
            card2 = self._player2[0]
            if len(self._player1) > card1 and len(self._player2) > card2:
                game = CardGame(self._player1[1:card1+1], self._player2[1:card2+1], recursive=True)
                round_winner = game.play()
        if round_winner == 0:
            round_winner = 1 if self._player1[0] > self._player2[0] else 2
        if round_winner == 1:
            self._move_card(self._player1, self._player2)
            return
        self._move_card(self._player2, self._player1)

    def play(self):
        while len(self._player1) > 0 and len(self._player2) > 0:
            if self._recursive and self._check_state():
                self._winner = 1
                break
            self._play_round()
        if self._winner == 0:
            if len(self._player1) > 0:
                self._winner = 1
            else:
                self._winner = 2
        return self._winner

    def calc_winning_score(self):
        cards = self._player1 if self._winner == 1 else self._player2
        n_cards = len(cards)
        result = 0
        for i in range(0, n_cards):
            result += cards[i] * (n_cards - i)
        return result


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)

    def _parse_data(self, raw_data):
        self._player1 = []
        self._player2 = []
        player = 1
        for line in raw_data:
            if len(line) == 0:
                player = 2
                continue
            if not line.isdigit():
                continue
            n = int(line)
            if player == 1:
                self._player1.append(n)
            else:
                self._player2.append(n)

    def do_part1(self):
        game = CardGame(self._player1[:], self._player2[:])
        game.play()
        return game.calc_winning_score()

    def do_part2(self):
        game = CardGame(self._player1[:], self._player2[:], recursive=True)
        game.play()
        return game.calc_winning_score()

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
