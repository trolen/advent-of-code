#! /usr/bin/env python3

class Firewall:
    def __init__(self, data_lines, max_ip):
        self._max_ip = max_ip
        self._blocked = self._parse_data(data_lines)
        self._available = self._build_available()

    def _parse_data(self, lines):
        blocked = []
        for line in lines:
            x,y = line.split('-')
            blocked.append((int(x),int(y)))
        return blocked

    def _build_available(self):
        available = [(0, self._max_ip)]
        for Bx,By in self._blocked:
            new_available = []
            for Ax,Ay in available:
                if Bx <= Ax and Ay <= By:
                    continue
                if By < Ax or Ay < Bx:
                    new_available.append((Ax, Ay))
                    continue
                if Ax < Bx and By < Ay:
                    new_available.append((Ax, Bx - 1))
                    new_available.append((By + 1, Ay))
                    continue
                if Bx <= Ax and Ax <= By:
                    Ax = By + 1
                if Bx <= Ay and Ay <= By:
                    Ay = Bx - 1
                new_available.append((Ax, Ay))
            available = new_available
        return available

    def find_first_available(self):
        return self._available[0][0]

    def count_available(self):
        result = 0
        for x,y in self._available:
            result += y - x + 1
        return result


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    firewall = Firewall(data, 4294967295)
    print('Part One: {0}'.format(firewall.find_first_available()))
    print('Part Two: {0}'.format(firewall.count_available()))
