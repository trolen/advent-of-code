import day01
import unittest


class TestDay01(unittest.TestCase):
    def test_part1(self):
        raw_input = [
            '1abc2',
            'pqr3stu8vwx',
            'a1b2c3d4e5f',
            'treb7uchet'
        ]
        app = day01.Application(raw_input)
        self.assertEqual(142, app.do_part1())

    def test_part2(self):
        raw_input = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen'
        ]
        app = day01.Application(raw_input)
        self.assertEqual(281, app.do_part2())


if __name__ == '__main__':
    unittest.main()
