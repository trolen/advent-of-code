#! /usr/bin/env python3

import unittest
import day21


class TestDay21(unittest.TestCase):
    def setUp(self):
        raw_data = [
            'mxmxvkd kfcds sqjhc nhms (contains dairy, fish)',
            'trh fvjkl sbzzf mxmxvkd (contains dairy)',
            'sqjhc fvjkl (contains soy)',
            'sqjhc mxmxvkd sbzzf (contains fish)'
        ]
        self.app = day21.Application(raw_data)
        self.part1_result = self.app.do_part1()

    def test_part1(self):
        self.assertEqual(5, self.part1_result)

    def test_part2(self):
        self.assertEqual('mxmxvkd,sqjhc,fvjkl', self.app.do_part2())


if __name__ == '__main__':
    unittest.main()
