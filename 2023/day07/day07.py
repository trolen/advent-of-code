def read_input(filename):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


FiveOfAKind = 7
FourOfAKind = 6
FullHouse = 5
ThreeOfAKind = 4
TwoPair = 3
Pair = 2
HighCard = 1


class Hand:
    def __init__(self, line, enableJokers=False):
        self._cardFaces = 'J23456789TQKA' if enableJokers else '23456789TJQKA'
        items = line.split(' ')
        self._cards = items[0]
        self.bet = int(items[1])
        self._set_type(enableJokers)
    
    def _set_type(self, enableJokers):
        counts = [self._cards.count(self._cardFaces[i]) for i in range(13)]
        if enableJokers and counts[0] > 0:
            maxCount = max(counts[1:])
            idx = counts[1:].index(maxCount) + 1
            counts[idx] += counts[0]
            counts[0] = 0
        self._type = HighCard
        if counts.count(5) > 0:
            self._type = FiveOfAKind
        elif counts.count(4) > 0:
            self._type = FourOfAKind
        elif counts.count(3) > 0:
            self._type = ThreeOfAKind
        pairs = counts.count(2)
        if pairs > 1:
            self._type = TwoPair
        elif pairs > 0:
            self._type = FullHouse if self._type == ThreeOfAKind else Pair

    def __eq__(self, other):
        return self._cards == other._cards

    def __lt__(self, other):
        if self._type != other._type:
            return self._type < other._type
        for i in range(5):
            if self._cards[i] == other._cards[i]:
                continue
            a = self._cardFaces.index(self._cards[i])
            b = self._cardFaces.index(other._cards[i])
            return a < b
        return False


class Application:
    def __init__(self, raw_input):
        self._raw_input = raw_input

    def _parse_input(self, enableJokers=False):
        self._hands = sorted([Hand(line, enableJokers) for line in self._raw_input])

    def _get_winnings(self):
        result = 0
        for i in range(len(self._hands)):
            result += self._hands[i].bet * (i + 1)
        return result

    def do_part1(self):
        self._parse_input()
        return self._get_winnings()

    def do_part2(self):
        self._parse_input(True)
        return self._get_winnings()


def main():
    raw_input = read_input('input.txt')
    app = Application(raw_input)
    print('Part 1:', app.do_part1())
    print('Part 2:', app.do_part2())


if __name__ == '__main__':
    main()
