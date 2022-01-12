#! /usr/bin/env python3


def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Caves:
  def __init__(self, raw_data):
    self._nodes = {}
    self._parse_data(raw_data)

  def _add_connection(self, node_a, node_b):
    if node_a not in self._nodes:
      self._nodes[node_a] = []
    if node_b not in self._nodes[node_a]:
      self._nodes[node_a].append(node_b)

  def _parse_data(self, raw_data):
    for line in raw_data:
      (node_a, node_b) = line.split('-')
      self._add_connection(node_a, node_b)
      self._add_connection(node_b, node_a)

  def count_paths(self, nodes_seen, current_node, allow_twice=False):
    if current_node == 'end':
      return 1
    if current_node.islower() and current_node in nodes_seen:
      if not allow_twice:
        return 0
      if current_node == 'start':
        return 0
      allow_twice=False
    new_nodes_seen = [n for n in nodes_seen]
    if current_node not in nodes_seen:
      new_nodes_seen.append(current_node)
    path_count = 0
    for node in self._nodes[current_node]:
      path_count += self.count_paths(new_nodes_seen, node, allow_twice)
    return path_count


def do_part1(raw_data):
  caves = Caves(raw_data)
  return caves.count_paths([], 'start')


def do_part2(raw_data):
  caves = Caves(raw_data)
  return caves.count_paths([], 'start', allow_twice=True)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
