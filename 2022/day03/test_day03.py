import day03
import unittest


class TestDay03 (unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]
        self._app = day03.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual(157, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(70, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
