#!/usr/bin/env python3

import hashlib
import time

def starts_with_zeros(digest, num_zeros):
  i = 0
  while num_zeros > 0:
    c = digest[i] if num_zeros >= 2 else digest[i] & 0xf0
    if c != 0:
      return False
    i += 1
    num_zeros -= 2
  return True

def find_hash(prefix, num_zeros):
  prefix_hash = hashlib.md5(prefix.encode())
  num = 0
  while True:
    new_hash = prefix_hash.copy()
    new_hash.update(str(num).encode())
    if starts_with_zeros(new_hash.digest(), num_zeros):
      return num, new_hash.hexdigest()
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
