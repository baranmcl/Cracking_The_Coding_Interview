#Design an algorithm to figure out if someone has one a game of tic-tac-toe.
#3x3 Board

board = [["o","x","o"], ["x","o","x"], ["x","o","x"]]

def checkWin(board):
  if ((board[0][0] == board[0][1] == board[0][2]) | (board[1][0] == board[1][1] == board[1][2]) | (board[2][0] == board[2][1] == board[2][2])):
    return True #checks rows
  elif ((board[0][0] == board[1][0] == board[2][0]) | (board[0][1] == board[1][1] == board[2][1]) | (board[0][2] == board[1][2] == board[2][2])):
    return True #checks columns
  elif ((board[0][0] == board[1][1] == board[2][2]) | (board[0][2] == board[1][1] == board[2][0])):
    return True #checks diagonals
  else:
    return False

print(checkWin(board))
