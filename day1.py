#!/usr/bin/python

INPUT_FILE="day1_input.txt"

def main():
  floor = 0
  position = 0
  positionEnterBasement = 0
  with open(INPUT_FILE, 'r') as f:
    data = f.read()
    for c in data:
      if c == '(':
        floor += 1
      if c == ')':
        floor -= 1
      position += 1
      if floor < 0 and positionEnterBasement <= 0:
        positionEnterBasement = position
  print "Floor:", floor
  print "Entered Basement at Position:", positionEnterBasement

if __name__ == "__main__":
  main()
