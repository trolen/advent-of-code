#!/usr/bin/env python3

def factors(n):
  result = []
  for i in range(1, int(n ** 0.5) + 1):
    if (n % i == 0):
      result += [i, int(n/i)]
  return sorted(list(set(result)))

def presents(house, method):
  result = 0
  if method == 1:
    result = sum(factors(house)) * 10
  elif method == 2:
    f = [x for x in factors(house) if x > int(house/50)]
    result = sum(f) * 11
  return result

def find_house(num_presents, method):
  h = 1
  n = presents(h, method)
  while n < num_presents:
    h += 1
    n = presents(h, method)
  return h

if __name__ == "__main__":
  n = 36000000
  print("First house to get %s presents (part 1): %s" % (n, find_house(n, 1)))
  print("First house to get %s presents (part 2): %s" % (n, find_house(n, 2)))
