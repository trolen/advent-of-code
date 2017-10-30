#! /usr/bin/env python3

import unittest
import day17

class TestDay17(unittest.TestCase):
    def test_path_code(self):
        vault = day17.Vault('hijkl')
        self.assertEqual('ced9', vault._get_path_code(''))
        self.assertEqual('f2bc', vault._get_path_code('D'))
        self.assertEqual('5745', vault._get_path_code('DR'))

    def test_open_doors(self):
        vault = day17.Vault('hijkl')
        self.assertEqual('UDL', vault._get_open_doors(''))
        self.assertEqual('ULR', vault._get_open_doors('D'))
        self.assertEqual('', vault._get_open_doors('DR'))

    def test_part1(self):
        vault = day17.Vault('ihgpwlah')
        self.assertEqual('DDRRRD', vault.find_shortest_path())
        vault = day17.Vault('kglvqrro')
        self.assertEqual('DDUDRLRRUDRD', vault.find_shortest_path())
        vault = day17.Vault('ulqzkmiv')
        self.assertEqual('DRURDRUDDLLDLUURRDULRLDUUDDDRR', vault.find_shortest_path())

    def test_part2(self):
        vault = day17.Vault('ihgpwlah')
        self.assertEqual(370, len(vault.find_longest_path()))
        vault = day17.Vault('kglvqrro')
        self.assertEqual(492, len(vault.find_longest_path()))
        vault = day17.Vault('ulqzkmiv')
        self.assertEqual(830, len(vault.find_longest_path()))


if __name__ == '__main__':
    unittest.main()
