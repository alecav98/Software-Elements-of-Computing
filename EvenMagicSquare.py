#  Description: In this assignment we will generate n magic squares of order 4
#  through permutation. N is decided by the user and is between 1 and 10 inclusive.

# Create global counter to keep track of squares printed
counter = 0

# Function will convert 1-D list to a 2-D list
def convert(perm_list):
  new_list = []
  list2 = []

  # Turn first four elements into their own list and append to list2
  for j in range(0, 4):
    new_list.append(perm_list[j])
  list2.append(new_list)
  new_list=[]

  # Turn next four elements into their own list and append to list2
  for j in range(4, 8):
    new_list.append(perm_list[j])
  list2.append(new_list)
  new_list=[]

  # Turn next four elements into their own list and append to list2
  for j in range(8, 12):
    new_list.append(perm_list[j])
  list2.append(new_list)
  new_list = []

  # Turn last four elements into their own list and append to list2
  for j in range(12, 16):
    new_list.append(perm_list[j])
  list2.append(new_list)
  new_list = []

  # Return list2, which is now a 2-D list
  return list2

# Print the magic square in a neat format where the numbers
# are right justified
def print_square (c):
    # use for loop to right adjust all elements and make all elements
    # in the same row a single string separated by a space
    for i in c:
        line = ' '.join([str(elem).rjust(5) for elem in i])
        print(line)

# Fuction will find as many permutations that create a magic square
# as the user inputs and print them out in a neat format
def permute(a, lo, num):
    global counter
    hi = len(a)
    if (lo == hi):
        # Create a copy of the permutation
        c = a[:]
        # Convert 1-D list into a 2-D list
        new_c = convert(c)
        # Print the 2-D list in a neat format
        print_square(new_c)
        # Print space in between squares
        print()
        counter += 1
        if counter == num:
            exit()
    else:
        for i in range(lo,hi):
            a[lo], a[i] = a[i], a[lo]
            # Check if the first row adds up to canonical sum
            if (lo == 3):
                if (sum(a[:4]) == 34):
                    permute(a[:], lo+1, num)
            # Check if the second row adds up to canonical sum
            elif (lo == 7):
                if (sum(a[4:8]) == 34):
                    permute(a[:], lo+1, num)
            # Check if 3rd row adds up to canonical sum
            elif (lo == 11):
                if (sum(a[8:12]) == 34):
                    permute(a[:], lo+1, num)
            # Check if 4th row adds up to canonical sum
            elif (lo == 15):
                if (sum(a[12:16]) == 34):
                    # Check if all the columns and both of the diagonals add up to canonical sum
                    if (((a[0] + a[4] + a[8] + a[12]) == 34) and ((a[1] + a[5] + a[9] + a[13])) and ((a[3] + a[6] + a[9] + a[12]) == 34)
                    and ((a[0] + a[5] + a[10] + a[15]) == 34) and ((a[1] + a[5] + a[9] + a[13]) == 34) and (a[3] + a[7] + a[11] + a[15]) == 34):
                        permute(a, lo+1, num)
            else:
                permute(a, lo+1, num)
            a[lo], a[i] = a[i], a[lo]

def main():
    # Ask user how many even magic squares they would like to see
    num = int(input('Enter number of magic squares (1 - 10): '))
    print()

    # Create initial list
    a = list(range(1,17))

    # Permute list and print out results
    permute(a,0,num)

main()
