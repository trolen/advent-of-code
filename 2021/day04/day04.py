#! /usr/bin/env python3

def read_data(filename):
  with open(filename, 'rt') as file:
    return [line.strip() for line in file.readlines()]


class Board:
  def __init__(self, data):
    self._board = []
    self._marks = []
    self._winner = False
    for line in data:
      row = []
      mark_row = []
      for item in line:
        row.append(item)
        mark_row.append(0)
      self._board.append(row)
      self._marks.append(mark_row)

  def _set_winner(self):
    nrows = len(self._board)
    ncols = len(self._board[0])
    for r in range(0, nrows):
      if sum(self._marks[r]) == ncols:
        self._winner = True
    for c in range(0, ncols):
      if sum([self._marks[r][c] for r in range(0, nrows)]) == nrows:
        self._winner = True

  def mark_number(self, number):
    nrows = len(self._board)
    for r in range(0, nrows):
      ncols = len(self._board[r])
      for c in range(0, ncols):
        if self._board[r][c] == number:
          self._marks[r][c] = 1
          self._set_winner()
          return

  def is_winner(self):
    return self._winner

  def score(self, number):
    n = 0
    for r in range(0, len(self._board)):
      for c in range(0, len(self._board[r])):
        if self._marks[r][c] == 0:
          n += self._board[r][c]
    return n * number


class Bingo:
  def __init__(self, raw_data):
    self._numbers = [int(x) for x in raw_data[0].split(',')]
    self._boards = []
    board_data = []
    for n in range(2, len(raw_data)):
      if len(raw_data[n]) == 0:
        self._boards.append(Board(board_data))
        board_data = []
        continue
      board_data.append([int(x) for x in raw_data[n].split()])
    self._boards.append(Board(board_data))

  def play(self, pick_last_board = False):
    last_board = None
    last_num = None
    for num in self._numbers:
      for board in self._boards:
        if board.is_winner():
          continue
        board.mark_number(num)
        if board.is_winner():
          if pick_last_board:
            last_board = board
            last_num = num
            continue
          return board.score(num)
    return last_board.score(last_num)


def do_part1(raw_data):
  bingo = Bingo(raw_data)
  return bingo.play()


def do_part2(raw_data):
  bingo = Bingo(raw_data)
  return bingo.play(pick_last_board=True)


def execute():
  raw_data = read_data('input.txt')
  print('Part 1 answer:', do_part1(raw_data))
  print('Part 2 answer:', do_part2(raw_data))


if __name__ == '__main__':
  execute()
