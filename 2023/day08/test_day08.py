import day08
import unittest

class TestDay08(unittest.TestCase):
    def setUp(self):
        self._raw_input1 = [
            'RL',
            '',
            'AAA = (BBB, CCC)',
            'BBB = (DDD, EEE)',
            'CCC = (ZZZ, GGG)',
            'DDD = (DDD, DDD)',
            'EEE = (EEE, EEE)',
            'GGG = (GGG, GGG)',
            'ZZZ = (ZZZ, ZZZ)'
        ]
        self._raw_input2 = [
            'LLR',
            '',
            'AAA = (BBB, BBB)',
            'BBB = (AAA, ZZZ)',
            'ZZZ = (ZZZ, ZZZ)'
        ]
        self._raw_input3 = [
            'LR',
            '',
            '11A = (11B, XXX)',
            '11B = (XXX, 11Z)',
            '11Z = (11B, XXX)',
            '22A = (22B, XXX)',
            '22B = (22C, 22C)',
            '22C = (22Z, 22Z)',
            '22Z = (22B, 22B)',
            'XXX = (XXX, XXX)'
        ]

    def test_part1(self):
        app1 = day08.Application(self._raw_input1)
        self.assertEqual(2, app1.do_part1())
        app2 = day08.Application(self._raw_input2)
        self.assertEqual(6, app2.do_part1())

    def test_part2(self):
        app = day08.Application(self._raw_input3)
        self.assertEqual(6, app.do_part2())


if __name__ == '__main__':
    unittest.main()
