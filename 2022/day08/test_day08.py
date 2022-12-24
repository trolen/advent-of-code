import day08
import unittest


class TestDay08(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '30373',
            '25512',
            '65332',
            '33549',
            '35390'
        ]
        self._app = day08.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual(21, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(8, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
