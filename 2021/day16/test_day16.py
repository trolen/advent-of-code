#! /usr/bin/env python3

import unittest
import day16


class TestDay16(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse_data(self):
        self.assertEqual('110100101111111000101000', day16.parse_data(['D2FE28']))
        self.assertEqual('11101110000000001101010000001100100000100011000001100000', day16.parse_data(['EE00D40C823060']))

    def test_version(self):
        packet = day16.Packet(day16.parse_data(['D2FE28']))
        self.assertEqual(6, packet.version())
        packet = day16.Packet(day16.parse_data(['38006F45291200']))
        self.assertEqual(1, packet.version())
        packet = day16.Packet(day16.parse_data(['EE00D40C823060']))
        self.assertEqual(7, packet.version())

    def test_type(self):
        packet = day16.Packet(day16.parse_data(['D2FE28']))
        self.assertEqual(4, packet.packet_type())
        packet = day16.Packet(day16.parse_data(['38006F45291200']))
        self.assertEqual(6, packet.packet_type())
        packet = day16.Packet(day16.parse_data(['EE00D40C823060']))
        self.assertEqual(3, packet.packet_type())

    def test_literal(self):
        packet = day16.Packet(day16.parse_data(['D2FE28']))
        self.assertEqual(2021, packet.literal())

    def test_length(self):
        packet = day16.Packet(day16.parse_data(['D2FE28']))
        self.assertEqual(21, packet.length())
        packet = day16.Packet(day16.parse_data(['38006F45291200']))
        self.assertEqual(49, packet.length())
        packet = day16.Packet(day16.parse_data(['EE00D40C823060']))
        self.assertEqual(51, packet.length())

    def test_part1(self):
        self.assertEqual(31, day16.do_part1(day16.parse_data(['A0016C880162017C3686B18A3D4780'])))

    def test_part2(self):
        self.assertEqual(1, day16.do_part2(day16.parse_data(['9C0141080250320F1802104A08'])))


if __name__ == '__main__':
    unittest.main()
