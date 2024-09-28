import day09
import unittest

class TestDay09(unittest.TestCase):
    def setUp(self):
        raw_input = [
            '0 3 6 9 12 15',
            '1 3 6 10 15 21',
            '10 13 16 21 30 45'
        ]
        self._app = day09.Application(raw_input)

    def test_part1(self):
        self.assertEqual(114, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(2, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
