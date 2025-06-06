import day03
import unittest

class TestDay03(unittest.TestCase):
    def setUp(self):
        raw_input = [
          'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
        ]
        self.app = day03.Application(raw_input)

    def test_part1(self):
        self.assertEqual(161, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(48, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
