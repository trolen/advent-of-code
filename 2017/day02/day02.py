#! /usr/bin/env pythone3

class Spreadsheet:
    def __init__(self, data):
        self._rows = []
        for line in data:
            self._rows.append([int(n) for n in line.split()])

    def get_checksum1(self):
        result = 0
        for r in self._rows:
            nMax = max(r)
            nMin = min(r)
            d = nMax - nMin
            result += d
        return result

    def get_checksum2(self):
        result = 0
        for r in self._rows:
            n = len(r)
            for i in range(n-1):
                n1 = r[i]
                for j in range(i+1, n):
                    n2 = r[j]
                    nMax = max(n1, n2)
                    nMin = min(n1, n2)
                    if (nMax % nMin) == 0:
                        result += nMax // nMin
                        i = n
                        j = n
        return result

def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]

if __name__ == '__main__':
    data = read_data('input.txt')
    spreadsheet = Spreadsheet(data)
    print('Part One: {0}'.format(spreadsheet.get_checksum1()))
    print('Part Two: {0}'.format(spreadsheet.get_checksum2()))
