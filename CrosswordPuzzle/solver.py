import os
import sys
import argparse
import utilities

def main():
  parser = utilities.get_arg_parser()
  args = parser.parse_args(sys.argv[1:])

  board = []
  if (os.path.exists(args.puzzlePath)):
    board = utilities.get_board_from_file(args.puzzlePath)
  else:
    print('Invalid path to crossword board')
    return
  
  words = []
  if (os.path.exists(args.wordsPath)):
    words = utilities.get_words_from_file(args.wordsPath)
  else:
    print('Invalid path to words')
    return

  solve(board, words)

def solve(board, words):
  global solved
  if len(words) == 0:
    if not solved:
      print_board(board)
    solved = True
    return

  if not solved:
    word = words.pop()
    for direction in get_possible_slots(board, word):
      fill(board, word, direction)
      solve(board, words)
      rollback(board, word, direction)
    words.append(word)

def get_possible_slots(board, word):
  length = len(word)
  rows = len(board)
  cols = len(board[0])

  for i in range(rows):
    for j in range(cols):

      horizontal_slot = True
      vertical_slot = True

      for k in range(length):
        if j < cols - length + 1:
          if board[i][j + k] not in ['_', word[k]]:
            horizontal_slot = False

        if i < rows - length + 1:
          if board[i + k][j] not in ['_', word[k]]:
            vertical_slot = False

      if horizontal_slot and j < cols - length + 1:
        yield (i, j, 0)
      if vertical_slot and i < rows - length + 1:
        yield (i, j, 1)

def fill(board, word, startLocation):
  i, j, axis = startLocation
  length = len(word)
  if axis == 0:
    for k in range(length):
      board[i][j + k] = word[k]
  else:
    for k in range(length):
      board[i + k][j] = word[k]

def rollback(board, word, startLocation):
  i, j, axis = startLocation
  length = len(word)
  if axis == 0:
    for k in range(length):
      board[i][j + k] = '_'
  else:
    for k in range(length):
      board[i + k][j] = '_'

def print_board(board):
  for row in board:
    print(''.join(row))

if __name__ == '__main__':
  solved = False
  main()
