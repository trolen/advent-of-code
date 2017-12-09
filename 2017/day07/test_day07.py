#! /usr/bin/env python3

import unittest
import day07

class TestDay7(unittest.TestCase):
    def setUp(self):
        data = [
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)'
        ]
        self._towers = day07.Towers(data)

    def test_get_root(self):
        self.assertEqual('tknk', self._towers.get_root())


if __name__ == '__main__':
    unittest.main()
