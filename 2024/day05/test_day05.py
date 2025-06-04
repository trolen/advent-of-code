import day05
import unittest

class TestDay05(unittest.TestCase):
    def setUp(self):
        raw_input1 = [
            '47|53',
            '97|13',
            '97|61',
            '97|47',
            '75|29',
            '61|13',
            '75|53',
            '29|13',
            '97|29',
            '53|29',
            '61|53',
            '97|53',
            '61|29',
            '47|13',
            '75|47',
            '97|75',
            '47|61',
            '75|61',
            '47|29',
            '75|13',
            '53|13',
            '',
            '75,47,61,53,29',
            '97,61,53,29,13',
            '75,29,13',
            '75,97,47,61,53',
            '61,13,29',
            '97,13,75,29,47'
        ]
        self.app = day05.Application(raw_input1)

    def test_part1(self):
        self.assertEqual(143, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(123, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
