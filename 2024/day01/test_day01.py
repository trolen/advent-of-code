import day01
import unittest

class TestDay01(unittest.TestCase):
    def setUp(self):
        raw_input = [
            '3   4',
            '4   3',
            '2   5',
            '1   3',
            '3   9',
            '3   3'
        ]
        self.app = day01.Application(raw_input)

    def test_part1(self):
        self.assertEqual(11, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(31, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
