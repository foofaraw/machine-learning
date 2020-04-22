import argparse

def get_arg_parser():
  parser = argparse.ArgumentParser(description='Solve NxM fill-in puzzle')
  parser.add_argument('puzzlePath', help='Path to the crossword board')
  parser.add_argument('wordsPath', help='Path to the list of words')
  return parser

def get_board_from_file(path):
  board = []
  with open(path, 'r') as f:
    line = f.readline()
    while line != '':
      board.append(list(line)[:-1])
      line = f.readline()
  return board