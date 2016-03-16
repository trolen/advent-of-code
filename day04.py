#!/usr/bin/env python3

import hashlib
import time

def find_hash(prefix, num_zeros):
  prefix_hash = hashlib.md5(prefix.encode())
  zeros = '0' * num_zeros
  num = 0
  while True:
    new_hash = prefix_hash.copy()
    new_hash.update(str(num).encode())
    hexdigest = new_hash.hexdigest()
    if hexdigest.startswith(zeros):
      return num, hexdigest
    num += 1
  return None

if __name__ == '__main__':
  prefix = 'iwrupvqb'
  t1 = time.time()
  num, hexdigest = find_hash(prefix, 5)
  t2 = time.time()
  print('For %s%s -> %s' % (prefix, num, hexdigest))
  print(' Time: %s sec' % (t2 - t1))
  t1 = time.time()
  num, hexdigest = find_hash(prefix, 6)
  t2 = time.time()
  print('For %s%s -> %s' % (prefix, num, hexdigest))
  print(' Time: %s sec' % (t2 - t1))
