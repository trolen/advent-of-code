import day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'Sabqponm',
            'abcryxxl',
            'accszExk',
            'acctuvwj',
            'abdefghi'
        ]
        self._app = day12.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual(31, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(29, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
