import day11
import unittest


class TestDay11(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'Monkey 0:',
            'Starting items: 79, 98',
            'Operation: new = old * 19',
            'Test: divisible by 23',
            'If true: throw to monkey 2',
            'If false: throw to monkey 3',
            '',
            'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
            'If true: throw to monkey 2',
            'If false: throw to monkey 0',
            '',
            'Monkey 2:',
            'Starting items: 79, 60, 97',
            'Operation: new = old * old',
            'Test: divisible by 13',
            'If true: throw to monkey 1',
            'If false: throw to monkey 3',
            '',
            'Monkey 3:',
            'Starting items: 74',
            'Operation: new = old + 3',
            'Test: divisible by 17',
            'If true: throw to monkey 0',
            'If false: throw to monkey 1'
        ]
        self._app = day11.Application()

    def test_part1(self):
        self.assertEqual(10605, self._app.do_part1(self._raw_input))

    def test_part2(self):
        self.assertEqual(2713310158, self._app.do_part2(self._raw_input))


if __name__ == '__main__':
    unittest.main()
