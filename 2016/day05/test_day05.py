#! /usr/bin/env python3

# THIS PROGRAM RUNS FASTER AT THE COMMAND PROMPT (NOT IN THE IDE)
# THE MD5 HAS ROUTINE IS SLOW

import unittest
import day05


class TestDay5(unittest.TestCase):
    def test_compute_hash(self):
        self.assertEqual(day05.compute_hash('abc3231929'), '00000155f8105dff7f56ee10fa9b9abd')

    def test_get_password1(self):
        self.assertEqual(day05.get_password1('abc'), '18f47a30')

    def test_get_password2(self):
        self.assertEqual(day05.get_password2('abc'), '05ace8e3')


if __name__ == '__main__':
    unittest.main()
