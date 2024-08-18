import day06
import unittest


class TestDay06(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'Time:      7  15   30',
            'Distance:  9  40  200'
        ]

    def test_part1(self):
        app = day06.Application(self._raw_input)
        self.assertEqual(288, app.do_part1())

    def test_part2(self):
        app = day06.Application(self._raw_input)
        self.assertEqual(71503, app.do_part2())


if __name__ == '__main__':
    unittest.main()
