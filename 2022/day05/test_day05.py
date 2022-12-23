import day05
import unittest


class TestDay05(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3',
            '',
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2'
        ]
        self._app = day05.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual('CMZ', self._app.do_part1())

    def test_part2(self):
        self.assertEqual('MCD', self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
