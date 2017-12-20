#! /usr/bin/env python3

import unittest
import day19

class TestDay19(unittest.TestCase):
    def setUp(self):
        data = [
            '     |          ',
            '     |  +--+    ',
            '     A  |  C    ',
            ' F---|----E|--+ ',
            '     |  |  |  D ',
            '     +B-+  +--+ '
        ]
        self._diagram = day19.Diagram(data)
        self._diagram.run()

    def test_part1(self):
        self.assertEqual('ABCDEF', self._diagram.path())

    def test_part2(self):
        self.assertEqual(38, self._diagram.steps())


if __name__ == '__main__':
    unittest.main()
