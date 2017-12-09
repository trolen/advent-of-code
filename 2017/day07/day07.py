#! /usr/bin/env python3

class Towers:
    def __init__(self, data):
        self._data = data
        self.reset()

    def reset(self):
        self._towers = []
        for line in self._data:
            terms = line.split()
            name,wt = terms[0], int(terms[1][1:-1])
            children = [t.strip(',') for t in terms[3:]]
            self._towers.append({'name':name, 'weight':wt, 'children':children, 'wt_children':0})
        self._root = self._find_root()
        self._calc_weights()

    def _find_root(self):
        result = ''
        for t in self._towers:
            if len(t['children']) == 0:
                continue
            name = t['name']
            found = False
            for t2 in self._towers:
                if name in t2['children']:
                    found = True
                    break
            if not found:
                result = name
                break
        return result

    def _find_node(self, name):
        for t in self._towers:
            if name == t['name']:
                return t
        return None

    def _sum_children(self, node):
        t = self._find_node(node)
        if t:
            t['wt_children'] = {}
            prev_wt = 0
            t['balanced'] = True
            for c in t['children']:
                wt = self._sum_children(c)
                t['wt_children'][c] = wt
                if prev_wt > 0 and prev_wt != wt:
                    t['balanced'] = False
                prev_wt = wt
            return t['weight'] + sum(t['wt_children'].values())
        return 0

    def _calc_weights(self):
        self._sum_children(self._root)

    def get_root(self):
        return self._root


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    towers = Towers(data)
    print('Part One: {0}'.format(towers.get_root()))
