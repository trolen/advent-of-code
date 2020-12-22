#! /usr/bin/env python3


class Application:
    def __init__(self, raw_data):
        self._parse_data(raw_data)
        self._monster = [
            '                  # ',
            '#    ##    ##    ###',
            ' #  #  #  #  #  #   '
        ]

    def _encode_side(self, line):
        n1 = 0
        n2 = 0
        l = len(line)
        for i in range(0, l):
            if line[i] == '#':
                n1 += 1 << (l - 1 - i)
                n2 += 1 << i
        return (n1, n2)

    def _parse_tile(self, lines):
        result = {}
        result['data'] = lines
        result['top'] = self._encode_side(lines[0])
        result['bottom'] = self._encode_side(lines[-1])
        result['left'] = self._encode_side([line[0] for line in lines])
        result['right'] = self._encode_side([line[-1] for line in lines])
        result['placed'] = False
        return result

    def _parse_data(self, raw_data):
        self._tiles = {}
        tile_num = 0
        tile_lines = []
        for line in raw_data:
            if line[:4] == 'Tile':
                tile_num = int(line[5:-1])
                continue
            if len(line) > 0:
                tile_lines.append(line)
                continue
            self._tiles[tile_num] = self._parse_tile(tile_lines)
            tile_lines = []

    def _flip_horizontal_array(self, data):
        return [line[::-1] for line in data]

    def _flip_horizontal_tile(self, key):
        data = self._flip_horizontal_array(self._tiles[key]['data'])
        self._tiles[key] = self._parse_tile(data)

    def _flip_vertical_array(self, data):
        return data[::-1]

    def _flip_vertical_tile(self, key):
        data = self._flip_vertical_array(self._tiles[key]['data'])
        self._tiles[key] = self._parse_tile(data)

    def _rotate_array(self, data):
        return [''.join([line[i] for line in data[::-1]]) for i in range(0, len(data[0]))]

    def _rotate_tile(self, key):
        data = self._rotate_array(self._tiles[key]['data'])
        self._tiles[key] = self._parse_tile(data)

    def _place_top_row(self, key):
        for t in self._grid[0]:
            (a1, a2) = self._tiles[t]['top']
            (b1, b2) = self._tiles[key]['left']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['right']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['top']
            if a1 in (b1, b2):
                self._flip_vertical_tile(key)
            (b1, b2) = self._tiles[key]['bottom']
            if a1 == b2:
                self._flip_horizontal_tile(key)
                (b1, b2) = self._tiles[key]['bottom']
            if a1 == b1:
                self._grid.insert(0, [key])
                self._tiles[key]['placed'] = True
                return True
        return False

    def _place_bottom_row(self, key):
        for t in self._grid[-1]:
            (a1, a2) = self._tiles[t]['bottom']
            (b1, b2) = self._tiles[key]['left']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['right']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['bottom']
            if a1 in (b1, b2):
                self._flip_vertical_tile(key)
            (b1, b2) = self._tiles[key]['top']
            if a1 == b2:
                self._flip_horizontal_tile(key)
                (b1, b2) = self._tiles[key]['top']
            if a1 == b1:
                self._grid.append([key])
                self._tiles[key]['placed'] = True
                return True
        return False

    def _place_left_side(self, key):
        for r in range(0, len(self._grid)):
            t = self._grid[r][0]
            (a1, a2) = self._tiles[t]['left']
            (b1, b2) = self._tiles[key]['top']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['bottom']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['left']
            if a1 in (b1, b2):
                self._flip_horizontal_tile(key)
            (b1, b2) = self._tiles[key]['right']
            if a1 == b2:
                self._flip_vertical_tile(key)
                (b1, b2) = self._tiles[key]['right']
            if a1 == b1:
                self._grid[r].insert(0, key)
                self._tiles[key]['placed'] = True
                return True
        return False

    def _place_right_side(self, key):
        for r in range(0, len(self._grid)):
            t = self._grid[r][-1]
            (a1, a2) = self._tiles[t]['right']
            (b1, b2) = self._tiles[key]['top']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['bottom']
            if a1 in (b1, b2):
                self._rotate_tile(key)
            (b1, b2) = self._tiles[key]['right']
            if a1 in (b1, b2):
                self._flip_horizontal_tile(key)
            (b1, b2) = self._tiles[key]['left']
            if a1 == b2:
                self._flip_vertical_tile(key)
                (b1, b2) = self._tiles[key]['left']
            if a1 == b1:
                self._grid[r].append(key)
                self._tiles[key]['placed'] = True
                return True
        return False

    def _place_tile(self, key):
        if len(self._grid) == 0:
            self._grid.append([key])
            self._tiles[key]['placed'] = True
            return True
        if self._place_top_row(key):
            return True
        if self._place_bottom_row(key):
            return True
        if self._place_left_side(key):
            return True
        if self._place_right_side(key):
            return True
        return False

    def _place_tiles(self):
        self._grid = []
        any_tile_placed = True
        while any_tile_placed:
            any_tile_placed = False
            for key in self._tiles:
                if self._tiles[key]['placed']:
                    continue
                if self._place_tile(key):
                    any_tile_placed = True
        for key in self._tiles:
            if not self._tiles[key]['placed']:
                return False
        return True

    def _corner_product(self):
        if len(self._grid) == 0:
            return 0
        result = self._grid[0][0] * self._grid[0][-1]
        result *= self._grid[-1][0] * self._grid[-1][-1]
        return result

    def do_part1(self):
        if self._place_tiles():
            return self._corner_product()
        return 0

    def _stitch_tiles(self):
        tile_rows = len(self._tiles[self._grid[0][0]]['data'])
        self._image = []
        for row in self._grid:
            for i in range(1, tile_rows - 1):
                new_row = ''
                for t in row:
                    new_row += self._tiles[t]['data'][i][1:-1]
                self._image.append(new_row)

    def _is_monster(self, offset1, offset2):
        monster_height = len(self._monster)
        monster_width = len(self._monster[0])
        found = True
        for r in range(0, monster_height):
            for c in range(0, monster_width):
                ch1 = self._monster[r][c]
                ch2 = self._image[offset1 + r][offset2 + c]
                if ch1 == '#' and ch2 != '#':
                    found = False
                    break
            if not found:
                break
        return found

    def _mark_monster(self, offset1, offset2):
        monster_height = len(self._monster)
        monster_width = len(self._monster[0])
        for r in range(0, monster_height):
            for c in range(0, monster_width):
                ch = self._monster[r][c]
                if ch == '#':
                    s = self._image[offset1 + r]
                    self._image[offset1 + r] = s[:offset2 + c] + 'O' + s[offset2 + c + 1:]

    def _find_sea_monsters(self):
        image_height = len(self._image)
        image_width = len(self._image[0])
        monster_height = len(self._monster)
        monster_width = len(self._monster[0])
        if image_height < monster_height:
            return False
        if image_width < monster_width:
            return False
        monster_found = False
        diff1 = image_height - monster_height
        diff2 = image_width - monster_width
        for r in range(0, diff1):
            for c in range(0, diff2):
                if self._is_monster(r, c):
                    self._mark_monster(r, c)
                    monster_found = True
        return monster_found

    def _count_not_monster(self):
        return sum([row.count('#') for row in self._image])

    def do_part2(self):
        self._stitch_tiles()
        found = False
        for i in range(0, 2):
            for j in range(0, 4):
                if self._find_sea_monsters():
                    found = True
                    break
                self._image = self._rotate_array(self._image)
            if found:
                break
            self._image = self._flip_vertical_array(self._image)
        if not found:
            return 0
        return self._count_not_monster()

    def execute(self):
        print('Part 1 result:', self.do_part1())
        print('Part 2 result:', self.do_part2())


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
