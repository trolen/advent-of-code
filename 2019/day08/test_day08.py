#! /usr/env python3

import unittest
import day08


class TestDay07(unittest.TestCase):
    def test_part1(self):
        raw_data = '123456789012'
        layers = day08.parse_layers(raw_data, width=3, height=2)
        crc = day08.calc_crc(layers)
        self.assertEqual(1, crc)

    def test_part2(self):
        raw_data = '0222112222120000'
        layers = day08.parse_layers(raw_data, width=2, height=2)
        image = day08.decode_image(layers)
        self.assertEqual('0110', image)


if __name__ == '__main__':
    unittest.main()