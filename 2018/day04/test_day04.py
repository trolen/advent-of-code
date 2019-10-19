#! /usr/env python3

import day04
import unittest


class TestDay04(unittest.TestCase):
    def setUp(self):
        self._data = [
            '[1518-11-01 00:00] Guard #10 begins shift',
            '[1518-11-01 00:05] falls asleep',
            '[1518-11-01 00:25] wakes up',
            '[1518-11-01 00:30] falls asleep',
            '[1518-11-01 00:55] wakes up',
            '[1518-11-01 23:58] Guard #99 begins shift',
            '[1518-11-02 00:40] falls asleep',
            '[1518-11-02 00:50] wakes up',
            '[1518-11-03 00:05] Guard #10 begins shift',
            '[1518-11-03 00:24] falls asleep',
            '[1518-11-03 00:29] wakes up',
            '[1518-11-04 00:02] Guard #99 begins shift',
            '[1518-11-04 00:36] falls asleep',
            '[1518-11-04 00:46] wakes up',
            '[1518-11-05 00:03] Guard #99 begins shift',
            '[1518-11-05 00:45] falls asleep',
            '[1518-11-05 00:55] wakes up'
        ]
        self._sleep_times = day04.tabulate_sleep_times(self._data)

    def test_part1(self):
        guard = day04.guard_asleep_most(self._sleep_times)
        minute = day04.minute_most_asleep(guard, self._sleep_times)
        self.assertEqual(240, guard * minute)

    def test_part2(self):
        (guard, minute) = day04.guard_most_asleep_on_minute(self._sleep_times)
        self.assertEqual(4455, guard * minute)


if __name__ == '__main__':
    unittest.main()