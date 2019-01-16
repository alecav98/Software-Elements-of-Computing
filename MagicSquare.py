'''
  Description: This program will ask the user for an odd, positive, integer. Then
  it will check that the input is valid, if not the program will ask the user
  for a new input. If the input is valid, program will create a magic square,
  print the magic_square and check that the magic square is in fact a magic square.

'''
# Populate a 2-D list with numbers from 1 to n**2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    n = int(n)
    i = n-1
    j = int(n/2)
    magic_square = [[0] * n for i in range(n)]
    magic_square[i][j] = 1
    for c in range(2,((n*n)+1)):
        if magic_square[(i+1)%n][(j+1)%n] == 0:
            i = (i+1)%n
            j = (j+1)%n
            magic_square[i][j] = c
        else:
            i = (i - 1 + n)%n
            magic_square[i][j] = c
    return(magic_square)
  
# Print the magic square in a neat format where the numbers
# are right justified
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    # use for loop to right adjust all elements and make all elements
    # in the same row a single string separated by a space
    for i in magic_square:
        line = ' '.join([str(elem).rjust(5) for elem in i])
        print(line)

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    # first we calculate what the canonical sum is
    true_sum = (len(magic_square) * ((len(magic_square)**2) + 1)) / 2
    # Use for loop to check that all rows add up to canonical sum
    for i in range(len(magic_square)):
        row_sum = 0
        for j in range(len(magic_square)):
            row_sum += magic_square[i][j]
        if row_sum != true_sum:
            return False
    # Use for loop to check that all columns add up to canonical sum
    for j in range(len(magic_square)):
        col_sum = 0
        for i in range(len(magic_square)):
            col_sum += magic_square[i][j]
        if col_sum != true_sum:
            return False
    # Use for loop to check that the right diagonal adds up to canonical sum
    for i in range(len(magic_square)):
        diag_sum_right = 0
        if i == 0:
            for j in range(len(magic_square)):
                if i == 0:
                    diag_sum_right += magic_square[i][j]
            if diag_sum_right != true_sum:
                return False
        else:
            break
    # Use for loop to check that the left diagonal adds up to canonical sum
    for i in range(len(magic_square)):
        diag_sum_left = 0
        if i == 2:
            for j in range(len(magic_square),0,-1):
                if i == 2:
                    diag_sum_left += magic_square[i][j-1]
            if diag_sum_left == true_sum:
                return True
        else:
            break
    return True
  
def main():
  # Prompt the user to enter an odd number 1 or greater
  n = input('Please enter an odd number greater than or equal to 1:')
  # Check the user input
  try:
      if int(n) >=1:
          n = int(n)
          if n%2 == 0:
              raise Exception
          else:
              pass
          # Create the magic square
          magic_square = make_square ( n )
          # Print the magic square
          print_square ( magic_square )
          # Verify that it is a magic square
          if check_square ( magic_square ) == True:
              sum = (int(n)*(int(n)**2 + 1))/2
              print('This is a magic square and the canonical sum is {}'.format(sum))
          else:
              print('This is not a magic square')
      elif int(n) < 1:
          raise Exception
  except ValueError:
      main()
  except:
      main()
      
if __name__ == "__main__":
  main()
