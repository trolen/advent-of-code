#!/usr/bin/env python3

import hashlib

def find_hash(key, prefix):
  key_hash = hashlib.md5(key.encode())
  num = 0
  while True:
    new_hash = key_hash.copy()
    new_hash.update(str(num).encode())
    hash_string = new_hash.hexdigest()
    if hash_string.startswith(prefix):
      return (num, hash_string)
    num += 1
  return None

if __name__ == '__main__':
  secret_key = 'iwrupvqb'
  print('Secret key: %s' % secret_key)
  prefix = '00000'
  (num, hash_string) = find_hash(secret_key, prefix)
  print('For prefix "%s", found %s.' % (prefix, num))
  print('Resulting hash: %s' % hash_string)
  prefix = '000000'
  (num, hash_string) = find_hash(secret_key, prefix)
  print('For prefix "%s", found %s.' % (prefix, num))
  print('Resulting hash: %s' % hash_string)
