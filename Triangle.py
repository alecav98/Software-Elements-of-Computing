#  File: Triangle.py

#  Description: We will apply four different approaches to problem solving
#  - exhaustive search, greedy, divide and conquer (recursive),
#  and dynamic programming - to find the greatest path sum starting at
#  the top of the triangle and moving only to adjacent numbers on the row below.

#  Student's Name: Jorge Caviedes

#  Student's UT EID: jac9773

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 10/29/2018

#  Date Last Modified: 10/31/2018

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
  list_sums = []
  row = 0
  position = 0
  sum = 0

  # Call helper function
  brute_force_helper (grid, row, position, list_sums, sum)
  return max(list_sums)

def brute_force_helper (grid, row, position, list_sums, sum):
  # use recursion, go down left or down right
  if (row == len(grid)):
    list_sums.append(sum)
    #sum += grid[row][position]
    #return sum
  else:
    brute_force_helper(grid, row+1, position, list_sums, sum+(grid[row][position]))
    #print(sum1) #########
    brute_force_helper(grid, row+1, position+1, list_sums, sum+(grid[row][position]))
    #return list_sums.append()
    #return

# returns the greatest path sum using greedy approach
def greedy (grid):
  return greedy_helper(grid)

def greedy_helper(grid):
  # Set sum equal to the value at the top of the pyramid
  sum = int(grid[0][0])
  #print(sum)
  place = 0
  for i in range (1,len(grid)):
    # if left is greater than right, add it to the sum
    if grid[i][place] >= grid[i][place+1]:
      sum += int(grid[i][place])
    else:
      # If right is greater than left, add it to the sum and make that
      # the new place in the row
      sum += int(grid[i][place+1])
      place += 1

  return sum

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  row = 0
  position = 0
  sum = 0
  # Call helper function
  return divide_conquer_helper(grid, row, position, sum)

def divide_conquer_helper (grid, row, position, sum):
  if (row == len(grid)):
    return 0
    #sum += grid[row][position]
    #return sum
  else:
    # Recursively compute value of left triangle
    sum1 = grid[row][position] + divide_conquer_helper(grid, row+1, position, sum)
    #print(sum1) #########

    # Recursively compute value of right triangle
    sum2 = grid[row][position] + divide_conquer_helper(grid, row+1, position+1, sum)

    # Return the triangle with the greatest sum
    return max(sum1, sum2)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return dynamic_prog_helper(grid)

def dynamic_prog_helper(grid):
  #sum = 0
  # Set i to be the last row of the pyramid
  i = len(grid)-1
  #for i in range(len(grid)-1):
  while i >= 0:
    # Check each pair in row, add value which is greater to
    # the corresponding value in the row above
    for j in range(len(grid[i])-1):
      if grid[i][j] >= grid[i][j+1]:
        grid[i-1][j] += grid[i][j]
      else:
        grid[i-1][j] += grid[i][j+1]

    # Move up one row
    i = i-1
  return int(grid[0][0])


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # open file for reading
  in_file = open("./triangle.txt", "r")

  # read first line
  line = in_file.readline()
  line = line.strip()
  num_lines = int(line)

  # create an empty list to represent triangle
  triangle = []

  # read each layer of the triangle from the file
  for line in range(num_lines):
    line = in_file.readline()
    line = line.strip()
    layer = line.split()
    for j in range(len(layer)):
      layer[j] = int(layer[j])

    triangle.append(layer)

  # Close the file
  in_file.close()

  return triangle

def main ():
  # First we must read triangular grid from file
  grid = read_file()
  print()

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The greatest path sum through exhaustive search is {}.'.format(brute_force(grid)))
  print('The time taken for exhaustive search is {} seconds.'.format(times))
  print()

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The greatest path sum through greedy search is {}.'.format(greedy(grid)))
  print('The time taken for greedy approach is {} seconds.'.format(times))
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The greatest path sum through recursive search is {}.'.format(divide_conquer(grid)))
  print('The time taken for recursive search is {} seconds.'.format(times))
  print()

  # output greatest path from dynamic programming
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The greatest path sum through dynamic programming is {}.'.format(dynamic_prog(grid)))
  print('The time taken for dynamic programming is {} seconds.'.format(times))

if __name__ == "__main__":
  main()
