#! /usr/bin/env python3

import codecs
import hashlib

class Vault:
    def __init__(self, passcode):
        self._passcode = passcode
        self.reset()

    def reset(self):
        self._open_nodes = [(0, 0, '')]
        self._found_path = None

    def _calculate_hash(self, s):
        digest = hashlib.md5(s.encode('utf-8')).digest()
        return codecs.encode(digest, 'hex').decode('utf-8')

    def _get_path_code(self, path):
        return self._calculate_hash(self._passcode + path)[:4]

    def _get_open_doors(self, path):
        code = self._get_path_code(path)
        doors = 'UDLR'
        return ''.join(doors[i] if code[i] in 'bcdef' else '' for i in range(len(doors)))

    def _save_path(self, path, find_longest):
        if self._found_path is None:
            self._found_path = path
        elif find_longest:
            if len(path) > len(self._found_path):
                self._found_path = path
        elif len(path) < len(self._found_path):
            self._found_path = path

    def _try_paths(self, find_longest):
        new_nodes = []
        for node in self._open_nodes:
            x = node[0]
            y = node[1]
            path = node[2]
            if not find_longest:
                if self._found_path is not None and len(path) >= len(self._found_path):
                    continue
            if x == 3 and y == 3:
                self._save_path(path, find_longest)
                continue
            open_doors = self._get_open_doors(path)
            if 'U' in open_doors and y > 0:
                new_nodes.append((x, y-1, path+'U'))
            if 'D' in open_doors and y < 3:
                new_nodes.append((x, y+1, path+'D'))
            if 'L' in open_doors and x > 0:
                new_nodes.append((x-1, y, path+'L'))
            if 'R' in open_doors and x < 3:
                new_nodes.append((x+1, y, path+'R'))
        self._open_nodes = new_nodes

    def _find_path(self, find_longest=False):
        while len(self._open_nodes) > 0:
            self._try_paths(find_longest)
        return self._found_path

    def find_shortest_path(self):
        return self._find_path()

    def find_longest_path(self):
        return self._find_path(True)


if __name__ == '__main__':
    passcode = 'pxxbnzuo'
    vault = Vault(passcode)
    print('Part One: {0}'.format(vault.find_shortest_path()))
    vault.reset()
    print('Part Two: {0}'.format(len(vault.find_longest_path())))
