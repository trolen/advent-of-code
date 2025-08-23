import day07
import unittest

class TestDay07(unittest.TestCase):
    def setUp(self):
        raw_input = [
            '190: 10 19',
            '3267: 81 40 27',
            '83: 17 5',
            '156: 15 6',
            '7290: 6 8 6 15',
            '161011: 16 10 13',
            '192: 17 8 14',
            '21037: 9 7 18 13',
            '292: 11 6 16 20'
        ]
        self.app = day07.Application(raw_input)

    def test_part1(self):
        self.assertEqual(3749, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(11387, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
