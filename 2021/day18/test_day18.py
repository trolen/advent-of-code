#! /usr/bin/env python3

import unittest
import day18


class TestDay18(unittest.TestCase):
    def setUp(self):
        self._raw_data = [
            '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
            '[[[5,[2,8]],4],[5,[[9,9],0]]]',
            '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
            '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
            '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
            '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
            '[[[[5,4],[7,7]],8],[[8,3],8]]',
            '[[9,3],[[9,9],[6,[4,9]]]]',
            '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
            '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'
        ]

    def test_addition(self):
        pair1 = day18.Pair('[[[[4,3],4],4],[7,[[8,4],9]]]')
        pair2 = day18.Pair('[1,1]')
        expected_result = day18.Pair('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
        self.assertEqual(expected_result, pair1 + pair2)

    def test_explode(self):
        pair = day18.Pair('[[[[[9,8],1],2],3],4]')
        pair._explode()
        expected_result = day18.Pair('[[[[0,9],2],3],4]')
        self.assertEqual(expected_result, pair)

    def test_split(self):
        pair = day18.Pair('[[[[0,7],4],[15,[0,13]]],[1,1]]')
        pair._split()
        expected_result = day18.Pair('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')
        self.assertEqual(expected_result, pair)
        pair._split()
        expected_result = day18.Pair('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]')
        self.assertEqual(expected_result, pair)

    def test_reduce(self):
        pair = day18.Pair('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
        pair.reduce()
        expected_result = day18.Pair('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]')
        self.assertEqual(expected_result, pair)
        pair1 = day18.Pair('[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]')
        pair2 = day18.Pair('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')
        result = pair1 + pair2
        result.reduce()
        expected_result = day18.Pair('[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]')
        self.assertEqual(expected_result, result)

    def test_magnitude(self):
        self.assertEqual(143, day18.Pair('[[1,2],[[3,4],5]]').magnitude())
        self.assertEqual(1384, day18.Pair('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]').magnitude())
        self.assertEqual(3488, day18.Pair('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]').magnitude())
        self.assertEqual(3993, day18.Pair('[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]').magnitude())

    def test_part1(self):
        self.assertEqual(4140, day18.do_part1(self._raw_data))

    def test_part2(self):
        self.assertEqual(3993, day18.do_part2(self._raw_data))


if __name__ == '__main__':
    unittest.main()
