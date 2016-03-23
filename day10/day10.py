#!/usr/bin/env python3

def looksay(s):
  result = ''
  group = ''
  for c in s:
    if len(group) > 0:
      if c == group[0]:
        group += c
      else:
        result += str(len(group)) + group[0]
        group = c
    else:
      group = c
  if len(group) > 0:
    result += str(len(group)) + group[0]
  return result

def looksay_repeat(s, n):
  for x in range(n):
    s = looksay(s)
  return s

if __name__ == "__main__":
  s = '1113222113'
  print("Length after 40 times: %s" % len(looksay_repeat(s, 40)))
  print("Length after 50 times: %s" % len(looksay_repeat(s, 50)))
