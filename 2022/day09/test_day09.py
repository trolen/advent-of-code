import day09
import unittest


class TestDay09(unittest.TestCase):
    def setUp(self):
        self._raw_input1 = [
            'R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2'
        ]
        self._raw_input2 = [
            'R 5',
            'U 8',
            'L 8',
            'D 3',
            'R 17',
            'D 10',
            'L 25',
            'U 20'
        ]
        self._app = day09.Application()

    def test_part1(self):
        self.assertEqual(13, self._app.do_part1(self._raw_input1))

    def test_part2(self):
        self.assertEqual(1, self._app.do_part2(self._raw_input1))
        self.assertEqual(36, self._app.do_part2(self._raw_input2))


if __name__ == '__main__':
    unittest.main()
