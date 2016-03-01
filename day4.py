#!/usr/bin/python

import md5

SECRET_KEY='iwrupvqb'

def find_hash(s):
  key_hash = md5.new(SECRET_KEY)
  i = 0
  while True:
    new_hash = key_hash.copy()
    new_hash.update(str(i))
    if new_hash.hexdigest().startswith(s):
      return i
    i += 1

if __name__ == '__main__':
  i1 = find_hash('00000')
  print 'Produces \'00000\' hash:', i1 
  i2 = find_hash('000000')
  print 'Produces \'000000\' hash:', i2 
