#! /usr/bin/env python3

from collections import Counter

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

    def _find_unbalanced(self):
        result = None
        for t in self._towers:
            if not t['balanced']:
                children_balanced = True
                for c in t['children']:
                    node = self._find_node(c)
                    children_balanced = children_balanced and node['balanced']
                if children_balanced:
                    result = t
                    break
        return result

    def _calc_adjustment(self, parent):
        counter = Counter(parent['wt_children'].values())
        child_adjust = None
        wt_adjust = 0
        wt_target = 0
        for child in parent['wt_children']:
            wt = parent['wt_children'][child]
            if counter[wt] == 1:
                wt_adjust = wt
                child_adjust = child
            else:
                wt_target = wt
        return (child_adjust, wt_target - wt_adjust)

    def balance(self):
        node = self._find_unbalanced()
        child_name, adjustment = self._calc_adjustment(node)
        child = self._find_node(child_name)
        return child['weight'] + adjustment


def read_data(filename):
    with open(filename, 'rt') as file:
        return [line.strip() for line in file]


if __name__ == '__main__':
    data = read_data('input.txt')
    towers = Towers(data)
    print('Part One: {0}'.format(towers.get_root()))
    print('Part Two: {0}'.format(towers.balance()))
