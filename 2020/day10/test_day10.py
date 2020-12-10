#! /usr/bin/env python3

import unittest
import day10


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.app1 = day10.Application([
            '16',
            '10',
            '15',
            '5',
            '1',
            '11',
            '7',
            '19',
            '6',
            '12',
            '4'
        ])
        self.app2 = day10.Application([
            '28',
            '33',
            '18',
            '42',
            '31',
            '14',
            '46',
            '20',
            '48',
            '47',
            '24',
            '23',
            '49',
            '45',
            '19',
            '38',
            '39',
            '11',
            '1',
            '32',
            '25',
            '35',
            '8',
            '17',
            '7',
            '9',
            '4',
            '2',
            '34',
            '10',
            '3'
        ])

    def test_part1(self):
        self.assertEqual(35, self.app1.do_part1())
        self.assertEqual(220, self.app2.do_part1())

    def test_part2(self):
        self.assertEqual(8, self.app1.do_part2())
        self.assertEqual(19208, self.app2.do_part2())


if __name__ == '__main__':
    unittest.main()
