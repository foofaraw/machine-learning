class Board:
  def __init__(self):
    self.board = [
      [0, 1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1, 0],
      [0, 1, 0, 1, 0, 1, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0],
      [2, 0, 2, 0, 2, 0, 2, 0],
      [0, 2, 0, 2, 0, 2, 0, 2],
      [2, 0, 2, 0, 2, 0, 2, 0]]
    
    self.turn = 1
    self.max_depth = 10

  def print(self):
    for row in self.board:
      for i in row:
       print(i, end=' ')
      print('\n')
  
  def get_winner(self):
    if self.board.count(2) == 0: return 1
    if self.board.count(1) == 0: return 2
    return 0
