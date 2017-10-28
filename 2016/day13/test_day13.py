import unittest
import day13

class TestDay13(unittest.TestCase):
    def test_part1(self):
        grid = day13.Grid(10, 1, 1)
        self.assertEqual(grid.find_shortest_path(7, 4), 11)


if __name__ == '__main__':
    unittest.main()
