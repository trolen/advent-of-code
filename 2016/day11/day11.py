#! /usr/bin/env python3

class Application:
    def __init__(self, raw_data):
        self._floor_grid = self._parse_data(raw_data)
        self._elevator = 0

    def _parse_data(self, raw_data):
        result = []
        for line in raw_data:
            floor = []
            terms = line.split(',')
            for term in terms:
                items = term.split(' and ')
                for item in items:
                    if len(item) == 0:
                        continue
                    words = item.split(' ')
                    element = words[-2]
                    if element == 'nothing':
                        continue
                    element = element[:2]
                    type = words[-1][0]
                    floor.append((element, type))
            result.append(floor)
        print(result)
        return result

    def _finished(self):
        for i in range(0, len(self._floor_grid) - 1):
            if len(self._floor_grid[i]) > 0:
                return False
        return True

    def execute(self):
        pass


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    app = Application(raw_data)
    app.execute()
