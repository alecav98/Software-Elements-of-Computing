#  Description: For the size of the board that the user specified, generate
#  and print all possible solutions to the queens problem for that size.

# make a global counter
counter = 0

class Queens (object):
  # initialize the board
  def __init__ (self, n = 8):
    self.board = []
    self.n = n
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()

  # check if no queen captures another
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True

  # do a recursive backtracking solution
  def recursive_solve (self, col):
    global counter
    if (col == self.n):
      # If we are here then we found an answer, so increase counter
      counter += 1

      # print board and add a space in between boards
      self.print_board()
      print()

    else:
      for i in range (self.n):
        if (self.is_valid(i, col)):
          # Change empty space to a Q
          self.board[i][col] = 'Q'

          # Try to find a solution recursively
          self.recursive_solve (col + 1)

          # Switch the value back to an empty space
          self.board[i][col] = '*'

  # if the problem has a solution print the board
  def solve (self, size):
    global counter

    # call recursive solve function, start it at 0th column
    self.recursive_solve(0)

    # print the number of solutions
    print('There are {} solutions for a(n) {} x {} board.'.format(counter, size, size))

def main():
  # Prompt the user to enter the size of the board.
  # Must be between 1 and 8 inclusive
  size = int(input('Enter the size of the board: '))
  while ((size < 1) or (size > 8)):
    size = int(input('Enter the size of the board: '))

  print()
  # create a chess board of size that the user input
  game = Queens (size)

  # place the queens on the board
  game.solve(size)

main()
