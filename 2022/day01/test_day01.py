import day01
import unittest


class TestDay01(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '1000',
            '2000',
            '3000',
            '',
            '4000',
            '',
            '5000',
            '6000',
            '',
            '7000',
            '8000',
            '9000',
            '',
            '10000'
        ]

    def test_part1(self):
        app = day01.Application(self._raw_input)
        self.assertEqual(24000, app.do_part1())

    def test_part2(self):
        app = day01.Application(self._raw_input)
        self.assertEqual(45000, app.do_part2())


if __name__ == '__main__':
    unittest.main()
