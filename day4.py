#!/usr/bin/python3

import hashlib

def find_hash(key, prefix):
  key_hash = hashlib.md5(key.encode())
  i = 0
  while True:
    new_hash = key_hash.copy()
    new_hash.update(str(i).encode())
    if new_hash.hexdigest().startswith(prefix):
      return i
    i += 1

if __name__ == '__main__':
  secret_key = 'iwrupvqb'
  print('Produces "00000" hash: %s' % find_hash(secret_key, '00000'))
  print('Produces "000000" hash: %s' % find_hash(secret_key, '000000'))
