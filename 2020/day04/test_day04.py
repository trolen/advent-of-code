#! /usr/bin/env python3

import unittest
import day04


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.raw_data = [
            'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
            'byr:1937 iyr:2017 cid:147 hgt:183cm',
            '',
            'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
            'hcl:#cfa07d byr:1929',
            '',
            'hcl:#ae17e1 iyr:2013',
            'eyr:2024',
            'ecl:brn pid:760753108 byr:1931',
            'hgt:179cm',
            '',
            'hcl:#cfa07d eyr:2025 pid:166559648'
            'iyr:2011 ecl:brn hgt:59in',
            '',
            'eyr:1972 cid:100',
            'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
            '',
            'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
            'hcl:#623a2f'
        ]
        self.passports = day04.parse_data(self.raw_data)

    def test_part1(self):
        self.assertEqual(4, day04.do_part1(self.passports))

    def test_byr(self):
        self.assertEqual(True, day04.is_valid_byr('2002'))
        self.assertEqual(False, day04.is_valid_byr('2003'))

    def test_hgt(self):
        self.assertEqual(True, day04.is_valid_hgt('60in'))
        self.assertEqual(True, day04.is_valid_hgt('190cm'))
        self.assertEqual(False, day04.is_valid_hgt('190in'))
        self.assertEqual(False, day04.is_valid_hgt('190'))

    def test_hcl(self):
        self.assertEqual(True, day04.is_valid_hcl('#123abc'))
        self.assertEqual(False, day04.is_valid_hcl('#123abz'))
        self.assertEqual(False, day04.is_valid_hcl('123abc'))
        self.assertEqual(False, day04.is_valid_hcl('#123'))

    def test_ecl(self):
        self.assertEqual(True, day04.is_valid_ecl('brn'))
        self.assertEqual(False, day04.is_valid_ecl('wat'))

    def test_pid(self):
        self.assertEqual(True, day04.is_valid_pid('000000001'))
        self.assertEqual(False, day04.is_valid_pid('0123456789'))

    def test_part2(self):
        self.assertEqual(3, day04.do_part2(self.passports))


if __name__ == '__main__':
    unittest.main()
