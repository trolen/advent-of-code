import day02
import unittest


class TestDay02(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]

    def test_part1(self):
        app = day02.Application(self._raw_input)
        self.assertEqual(8, app.do_part1())

    def test_part2(self):
        app = day02.Application(self._raw_input)
        self.assertEqual(2286, app.do_part2())


if __name__ == '__main__':
    unittest.main()
