#! /usr/bin/env python3

import unittest
import day09

class TestDay9(unittest.TestCase):
    def test_part1(self):
        stream = day09.Stream()
        stream.analyze('{}')
        self.assertEqual(1, stream.score())
        stream.analyze('{{{}}}')
        self.assertEqual(6, stream.score())
        stream.analyze('{{},{}}')
        self.assertEqual(5, stream.score())
        stream.analyze('{{{},{},{{}}}}')
        self.assertEqual(16, stream.score())
        stream.analyze('{<a>,<a>,<a>,<a>}')
        self.assertEqual(1, stream.score())
        stream.analyze('{{<ab>},{<ab>},{<ab>},{<ab>}}')
        self.assertEqual(9, stream.score())
        stream.analyze('{{<!!>},{<!!>},{<!!>},{<!!>}}')
        self.assertEqual(9, stream.score())
        stream.analyze('{{<a!>},{<a!>},{<a!>},{<ab>}}')
        self.assertEqual(3, stream.score())

    def test_part2(self):
        stream = day09.Stream()
        stream.analyze('{<>}')
        self.assertEqual(0, stream.garbage())
        stream.analyze('{<random characters>}')
        self.assertEqual(17, stream.garbage())
        stream.analyze('{<<<<>}')
        self.assertEqual(3, stream.garbage())
        stream.analyze('{<{!>}>}')
        self.assertEqual(2, stream.garbage())
        stream.analyze('{<!!>}')
        self.assertEqual(0, stream.garbage())
        stream.analyze('{<!!!>>}')
        self.assertEqual(0, stream.garbage())
        stream.analyze('{<{o"i!a,<{i<a>}')
        self.assertEqual(10, stream.garbage())


if __name__ == '__main__':
    unittest.main()
