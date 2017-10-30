#! /usr/bin/env python3

class RoomMap:
    def __init__(self, initial_row, num_rows):
        self._initial_row = initial_row
        self._num_rows = num_rows
        self._generate_room_map()

    def _generate_room_map(self):
        self._room_map = [self._initial_row]
        for prev_idx in range(self._num_rows - 1):
            prev_row = self._room_map[prev_idx]
            new_row = ''
            for idx in range(len(prev_row)):
                l_ch = prev_row[idx - 1] if idx > 0 else '.'
                c_ch = prev_row[idx]
                r_ch = prev_row[idx + 1] if idx < len(prev_row) - 1 else '.'
                pair = l_ch + r_ch
                if pair == '.^' or pair == '^.':
                    new_ch = '^'
                else:
                    new_ch = '.'
                new_row += new_ch
            self._room_map.append(new_row)

    def count_safe_tiles(self):
        result = 0
        for row in self._room_map:
            result += row.count('.')
        return result

if __name__ == '__main__':
    initial_row = '...^^^^^..^...^...^^^^^^...^.^^^.^.^.^^.^^^.....^.^^^...^^^^^^.....^.^^...^^^^^...^.^^^.^^......^^^^'
    room_map = RoomMap(initial_row, 40)
    print('Part One: {0}'.format(room_map.count_safe_tiles()))
    room_map = RoomMap(initial_row, 400000)
    print('Part Two: {0}'.format(room_map.count_safe_tiles()))
