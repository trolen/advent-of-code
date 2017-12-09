#! /usr/bin/env python3

import unittest
import day08

class TestDay8(unittest.TestCase):
    def setUp(self):
        data = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10'
        ]
        self._interpreter = day08.Interpreter(data)
        self._interpreter.run()

    def test_max_value(self):
        self.assertEqual(1, self._interpreter.max_register_value())

    def test_max_allocation(self):
        self.assertEqual(10, self._interpreter.max_allocation())


if __name__ == '__main__':
    unittest.main()
