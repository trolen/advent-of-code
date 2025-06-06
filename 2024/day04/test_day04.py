import day04
import unittest

class TestDay04(unittest.TestCase):
    def setUp(self):
        raw_input = [
            'MMMSXXMASM',
            'MSAMXMSMSA',
            'AMXSXMAAMM',
            'MSAMASMSMX',
            'XMASAMXAMM',
            'XXAMMXXAMA',
            'SMSMSASXSS',
            'SAXAMASAAA',
            'MAMMMXMMMM',
            'MXMXAXMASX'
        ]
        self.app = day04.Application(raw_input)

    def test_part1(self):
        self.assertEqual(18, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(9, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
