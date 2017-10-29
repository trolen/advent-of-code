#! /usr/bin/env python3

import codecs
import hashlib


class CommPad:
    def __init__(self, salt, stretching=False):
        self._salt = salt
        self.reset(stretching)

    def reset(self, stretching=False):
        self._hashes = []
        self._triples = []
        self._keys = []
        self._stretching = stretching

    def _calculate_hash(self, s):
        iterations = 2017 if self._stretching else 1
        for _ in range(iterations):
            digest = hashlib.md5(s.encode('utf-8')).digest()
            s = codecs.encode(digest, 'hex').decode('utf-8')
        return s

    def _get_hash(self, idx):
        n_hashes = len(self._hashes)
        while idx >= n_hashes:
            self._hashes.append(self._calculate_hash(self._salt + str(n_hashes)))
            n_hashes += 1
        return self._hashes[idx]

    def _check_triple(self, s):
        for i, c in enumerate(s):
            triple = ''.join(c * 3)
            if triple == s[i:i+3]:
                return (True, c)
        return (False, None)

    def _get_next_triple(self):
        idx = self._triples[-1][0] + 1 if len(self._triples) > 0 else 0
        while True:
            hash = self._get_hash(idx)
            is_triple, ch = self._check_triple(hash)
            if is_triple:
                self._triples.append((idx, ch))
                break
            idx += 1
        return self._triples[-1]

    def _is_key(self, triple):
        start = triple[0] + 1
        ch = triple[1]
        for i in range(start, start+1000):
            hash = self._get_hash(i)
            quint = ''.join(ch * 5)
            if quint in hash:
                return True
        return False

    def _get_next_key(self):
        while True:
            triple = self._get_next_triple()
            if self._is_key(triple):
                self._keys.append(triple[0])
                break
        return self._keys[-1]

    def find_keys(self, num_keys):
        while len(self._keys) < num_keys:
            self._get_next_key()
        return self._keys[-1]


if __name__ == '__main__':
    commpad = CommPad('qzyelonm')
    print('Part One: {0}'.format(commpad.find_keys(64)))
    commpad.reset(True)
    print('Part Two: {0}'.format(commpad.find_keys(64)))
