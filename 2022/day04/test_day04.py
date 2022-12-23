import day04
import unittest


class TestDay04(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8'
        ]
        self._app = day04.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual(2, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(4, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
