import sys


def printBoard(board):
  for row in board:
      print(''.join(row))


def possibleDirections(board, word):
  length = len(word)
  rows = len(board)
  cols = len(board[0])

  for i in range(rows):
      for j in range(cols):

          properSlotH = True
          properSlotV = True

          for k in range(length):
              #Horizontal direction, axis marked as 0:
              if j < cols - length + 1:
                  if board[i][j + k] not in ['_', word[k]]:
                      properSlotH = False

              #Vertival direction, axis marked as 1:
              if i < rows - length + 1:
                  if board[i + k][j] not in ['_', word[k]]:
                      properSlotV = False

          if properSlotH and j < cols - length+1:
              yield (i, j, 0)
          if properSlotV and i < rows - length+1:
              yield (i, j, 1)


def move(board, word, startLocation):
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


def solve(board, words):
  global solved
  if len(words) == 0:
      if not solved:
          printBoard(board)
      solved = True
      return

  word = words.pop()

  for direction in possibleDirections(board, word):
      move(board, word, direction)
      solve(board, words)
      rollback(board, word, direction)

  words.append(word)


if __name__ == '__main__':
  board = []
  with open('Data/puzzle2', 'r') as f:
    line = f.readline()
    while line != '':
      board.append(list(line)[:-1])
      line = f.readline()

  words = []
  with open('Data/words2', 'r') as f:
    words = f.read().splitlines()

  solved = False
  solve(board, words)
