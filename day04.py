#!/usr/bin/env python3

import hashlib
import time

def find_hash(key, prefix):
  key_hash = hashlib.md5(key.encode())
  num = 0
  while True:
    new_hash = key_hash.copy()
    new_hash.update(str(num).encode())
    hash_string = new_hash.hexdigest()
    if hash_string.startswith(prefix):
      return num, hash_string
    num += 1
  return None

if __name__ == '__main__':
  secret_key = 'iwrupvqb'
  t1 = time.time()
  num, hash_string = find_hash(secret_key, "00000")
  t2 = time.time()
  print('For %s%s -> %s' % (secret_key, num, hash_string))
  print(' Time: %s sec' % (t2 - t1))
  t1 = time.time()
  num, hash_string = find_hash(secret_key, '000000')
  t2 = time.time()
  print('For %s%s -> %s' % (secret_key, num, hash_string))
  print(' TIme: %s sec' % (t2 - t1))
