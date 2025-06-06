import day02
import unittest

class TestDay02(unittest.TestCase):
    def setUp(self):
        raw_input = [
          '7 6 4 2 1',
          '1 2 7 8 9',
          '9 7 6 2 1',
          '1 3 2 4 5',
          '8 6 4 4 1',
          '1 3 6 7 9'
        ]
        self.app = day02.Application(raw_input)

    def test_part1(self):
        self.assertEqual(2, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(4, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
