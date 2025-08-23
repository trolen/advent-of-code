import day06
import unittest

class TestDay06(unittest.TestCase):
    def setUp(self):
        raw_input = [
            '....#.....',
            '.........#',
            '..........',
            '..#.......',
            '.......#..',
            '..........',
            '.#..^.....',
            '........#.',
            '#.........',
            '......#...'
        ]
        self.app = day06.Application(raw_input)

    def test_part1(self):
        self.assertEqual(41, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(6, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
