import day07
import unittest


class TestDay07(unittest.TestCase):
    def setUp(self):
        self._raw_input = [
            '$ cd /',
            '$ ls',
            'dir a',
            '14848514 b.txt',
            '8504156 c.dat',
            'dir d',
            '$ cd a',
            '$ ls',
            'dir e',
            '29116 f',
            '2557 g',
            '62596 h.lst',
            '$ cd e',
            '$ ls',
            '584 i',
            '$ cd ..',
            '$ cd ..',
            '$ cd d',
            '$ ls',
            '4060174 j',
            '8033020 d.log',
            '5626152 d.ext',
            '7214296 k'
        ]
        self._app = day07.Application(self._raw_input)

    def test_part1(self):
        self.assertEqual(95437, self._app.do_part1())

    def test_part2(self):
        self.assertEqual(24933642, self._app.do_part2())


if __name__ == '__main__':
    unittest.main()
