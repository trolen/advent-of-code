import day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(7, day06.do_part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))
        self.assertEqual(5, day06.do_part1('bvwbjplbgvbhsrlpgdmjqwftvncz'))
        self.assertEqual(6, day06.do_part1('nppdvjthqldpwncqszvftbrmjlhg'))
        self.assertEqual(10, day06.do_part1('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
        self.assertEqual(11, day06.do_part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))

    def test_part2(self):
        self.assertEqual(19, day06.do_part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb'))
        self.assertEqual(23, day06.do_part2('bvwbjplbgvbhsrlpgdmjqwftvncz'))
        self.assertEqual(23, day06.do_part2('nppdvjthqldpwncqszvftbrmjlhg'))
        self.assertEqual(29, day06.do_part2('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))
        self.assertEqual(26, day06.do_part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))


if __name__ == '__main__':
    unittest.main()
