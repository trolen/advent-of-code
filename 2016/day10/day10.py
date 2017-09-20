#! /usr/bin/env python3


class Bot:
    def __init__(self):
        self._chips = []
        self.instructions = None

    def assign_chip(self, value):
        self._chips.append(value)

    def chip_count(self):
        return len(self._chips)

    def clear_chips(self):
        self._chips.clear()

    def compare_chips(self, v1, v2):
        self._chips.sort()
        chips = sorted([v1, v2])
        return self._chips[0] == chips[0] and self._chips[1] == chips[1]

    def set_instructions(self, instructions):
        self._instructions = instructions

    def interpret_instructions(self):
        return [(min(self._chips), self._instructions[5], self._instructions[6]),
                (max(self._chips), self._instructions[-2], self._instructions[-1])
                ]


class BalanceBots:
    def __init__(self, instructions):
        self._bots = {}
        self._output_bins = {}
        self._load_instructions(instructions)

    def _load_instructions(self, instructions):
        for instruction in instructions:
            terms = instruction.split()
            if terms[0] == 'value':
                bot = terms[-1]
                chip = int(terms[1])
                self._assign_chip(bot, chip)
            else:
                bot = terms[1]
                self._assign_instructions(bot, terms)

    def _create_bot_if_not_exists(self, bot):
        if bot not in self._bots:
            self._bots[bot] = Bot()

    def _assign_chip(self, bot, chip):
        self._create_bot_if_not_exists(bot)
        self._bots[bot].assign_chip(chip)

    def _assign_instructions(self, bot, instructions):
        self._create_bot_if_not_exists(bot)
        self._bots[bot].set_instructions(instructions)

    def _find_full_bot(self):
        for bot in self._bots:
            if self._bots[bot].chip_count() == 2:
                return bot
        return None

    def _follow_instructions(self, bot):
        for cmd in self._bots[bot].interpret_instructions():
            if cmd[1] == 'bot':
                self._assign_chip(cmd[2], cmd[0])
            else:
                self._output_bins[cmd[2]] = cmd[0]
        self._bots[bot].clear_chips()

    def _get_next_full_bot(self):
        while True:
            bot = self._find_full_bot()
            if bot is None:
                break
            yield bot

    def run_part1(self, v1, v2):
        for bot in self._get_next_full_bot():
            if self._bots[bot].compare_chips(v1, v2):
                return bot
            self._follow_instructions(bot)
        return None

    def run_part2(self):
        for bot in self._get_next_full_bot():
            self._follow_instructions(bot)
        return self._output_bins['0'] * self._output_bins['1'] * self._output_bins['2']


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    instructions = read_data('input.txt')
    balance_bots1 = BalanceBots(instructions)
    print('Part One: {0}'.format(balance_bots1.run_part1(17, 61)))
    balance_bots2 = BalanceBots(instructions)
    print('Part Two: {0}'.format(balance_bots2.run_part2()))
