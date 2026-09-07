import day01
import unittest

class TestDay01(unittest.TestCase):
    def setUp(self):
        raw_input = [
            'L68',
            'L30',
            'R48',
            'L5',
            'R60',
            'L55',
            'L1',
            'L99',
            'R14',
            'L82'
        ]
        self.app = day01.Application(raw_input)

    def test_part1(self):
        self.assertEqual(3, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(6, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
