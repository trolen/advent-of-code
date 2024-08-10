import day03
import unittest


class TestDay03(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '467..114..',
            '...*......',
            '..35..633.',
            '......#...',
            '617*......',
            '.....+.58.',
            '..592.....',
            '......755.',
            '...$.*....',
            '.664.598..',
        ]

    def test_part1(self):
        app = day03.Application(self._raw_input)
        self.assertEqual(4361, app.do_part1())

    #def test_part2(self):
    #    app = day03.Application(self._raw_input)
    #    self.assertEqual(2286, app.do_part2())


if __name__ == '__main__':
    unittest.main()
