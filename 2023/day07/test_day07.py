import day07
import unittest

class TestDay07(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '32T3K 765',
            'T55J5 684',
            'KK677 28',
            'KTJJT 220',
            'QQQJA 483'
        ]

    def test_part1(self):
        app = day07.Application(self._raw_input)
        self.assertEqual(6440, app.do_part1())

    def test_part2(self):
        app = day07.Application(self._raw_input)
        self.assertEqual(5905, app.do_part2())


if __name__ == '__main__':
    unittest.main()
