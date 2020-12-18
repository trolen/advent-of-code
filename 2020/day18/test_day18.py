#! /usr/bin/env python3

import unittest
import day18


class TestDay18(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            '1 + 2 * 3 + 4 * 5 + 6',
            '2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        ]
        self.app = day18.Application(self.raw_data)

    def test_eval_expression(self):
        self.assertEqual(71, self.app._evaluate_expression(
            ['1','+','2','*','3','+','4','*','5','+','6']
        ))
        self.assertEqual(51, self.app._evaluate_expression(
            ['1','+','(','2','*','3',')','+','(','4','*','(','5','+','6',')',')']
        ))
        self.assertEqual(231, self.app._evaluate_expression(
            ['1','+','2','*','3','+','4','*','5','+','6'], 2
        ))
        self.assertEqual(51, self.app._evaluate_expression(
            ['1','+','(','2','*','3',')','+','(','4','*','(','5','+','6',')',')'], 2
        ))

    def test_part1(self):
        self.assertEqual(26406, self.app.do_part1())

    def test_part2(self):
        self.assertEqual(694122, self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
