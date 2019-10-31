#! /usr/env python3

import day14
import unittest


class TestDay14(unittest.TestCase):
    def test_part1(self):
        s = day14.generate_recipes1(9)
        self.assertEqual('5158916779', s)
        s = day14.generate_recipes1(5)
        self.assertEqual('0124515891', s)
        s = day14.generate_recipes1(18)
        self.assertEqual('9251071085', s)
        s = day14.generate_recipes1(2018)
        self.assertEqual('5941429882', s)

    def test_part2(self):
        n = day14.generate_recipes2('51589')
        self.assertEqual(9, n)
        n = day14.generate_recipes2('01245')
        self.assertEqual(5, n)
        n = day14.generate_recipes2('92510')
        self.assertEqual(18, n)
        n = day14.generate_recipes2('59414')
        self.assertEqual(2018, n)


if __name__ == '__main__':
    unittest.main()
