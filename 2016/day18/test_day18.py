#! /usr/bin/env python3

import unittest
import day18

class TestDay18(unittest.TestCase):
    def test_small_room(self):
        room_map = day18.RoomMap('..^^.', 3)
        self.assertEqual(6, room_map.count_safe_tiles())

    def test_large_room(self):
        room_map = day18.RoomMap('.^^.^.^^^^', 10)
        self.assertEqual(38, room_map.count_safe_tiles())

if __name__ == '__main__':
    unittest.main()
