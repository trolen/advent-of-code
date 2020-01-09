#! /usr/env python3

import unittest
import day09


class TestDay09(unittest.TestCase):
    def test_part1(self):
        data = day09.run_intcode('1002,4,3,4,33')
        self.assertEqual([1002, 4, 3, 4, 99], data)
        data = day09.run_intcode('1101,100,-1,4,0')
        self.assertEqual([1101, 100, -1, 4, 99], data)
        data = day09.run_intcode('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
        expected_result = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 16, 1]
        self.assertEqual(expected_result, data)
        data = day09.run_intcode('1102,34915192,34915192,7,4,7,99,0')
        self.assertEqual([1102,34915192,34915192,7,4,7,99,1219070632396864], data)
        data = day09.run_intcode('104,1125899906842624,99')
        self.assertEqual([104,1125899906842624,99], data)

    def test_part2(self):
        pass


if __name__ == '__main__':
    unittest.main()