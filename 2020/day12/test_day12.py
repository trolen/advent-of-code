#! /usr/bin/env python3

import unittest
import day12


class TestDay12(unittest.TestCase):
    def setUp(self):
        pass
        self._app = day12.Application([
            'F10',
            'N3',
            'F7',
            'R90',
            'F11'
        ])

    def test_part1(self):
        self.assertEqual(25, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(286, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
