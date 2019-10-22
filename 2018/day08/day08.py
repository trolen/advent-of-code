#! /usr/bin/env python3

from datetime import datetime

class Node:
    def __init__(self, data):
        self._num_children = data[0]
        self._len_metadata = data[1]
        self._children = []
        offset = 2
        for i in range(0, self._num_children):
            child = Node(data[offset:])
            self._children.append(child)
            offset += child.size()
        self._size = offset + self._len_metadata
        self._metadata = []
        for i in range(offset, self._size):
            self._metadata.append(data[i])

    def size(self):
        return self._size

    def children(self):
        return self._children

    def metadata(self):
        return self._metadata

    def value(self):
        if self._num_children == 0:
            return sum(self._metadata)
        result = 0
        for n in self._metadata:
            idx = n - 1
            if 0 <= idx and idx < self._num_children:
                result += self._children[idx].value()
        return result


def read_data(filename):
    with open(filename, 'rt') as file:
        return file.readline().strip()


def parse_nodes(raw_data):
    numbers = [int(x) for x in raw_data.split(' ')]
    results = Node(numbers)
    return results


def sum_metadata(root_node):
    result = 0
    for child in root_node.children():
        result += sum_metadata(child)
    result += sum(root_node.metadata())
    return result


def calc_value(root_node):
    return root_node.value()


if __name__ == '__main__':
    raw_data = read_data('input.txt')
    nodes = parse_nodes(raw_data)
    n = sum_metadata(nodes)
    print('Sum Metadata: {0}'.format(n))
    n = calc_value(nodes)
    print('Value: {0}'.format(n))
