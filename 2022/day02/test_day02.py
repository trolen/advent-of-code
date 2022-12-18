import day02
import unittest


class TestDay02(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'A Y',
            'B X',
            'C Z'
        ]
        self._app = day02.Application(self._raw_input)

    def TestPart1(self):
        self.assertEqual(15, self._app.do_part1())

    def TestPart2(self):
        self.assertEqual(12, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
