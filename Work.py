#  File: Work.py

#  Description: Use the Binary Search algorithm to find how many
#  lines Vyasa has to write before having his first cup of coffee.

#  Student Name: Jorge Caviedes

#  Student UT EID: jac9773

#  Course Name: CS 313E

#  Unique Number: 53150

#  Date Created: 10/6/2018

#  Date Last Modified: 10/8/2018

# This function will give back a list of the sums starting from
# v = 1 to v = n - 1
def calcSum (mid,k):
  sum = mid
  j = 1
  while (mid//(k**j)) > 0:
    sum += mid//(k**j)
    j += 1
  return sum

# This function will find and return the index whose sum is
# equal to n or is the smallest value greater than n.
def binarySearch (n, k): # (a, x)
  #n_list = calcSum(n,k)
  #print(n_list)
  lo = 0
  hi = n - 1
  while (lo <= hi):
    mid = (lo + hi) // 2
    if (n > calcSum(mid,k)): #n_list[mid]):
      lo = mid + 1
    elif (n < calcSum(mid,k)):# n_list[mid]):
      hi = mid - 1
    else:
      return mid
  return lo #return -1


def main():
  in_file = open('./work.txt', 'r')
  num_cases = int(in_file.readline())
  for i in range(num_cases):
    line = in_file.readline()
    if line == '':
      break
    else:
      # num lines of code to write (1 ≤ n ≤ 106)
      n = int(line.split(' ')[0])
      # productivity factor (2 ≤ k ≤ 10)
      k = int(line.split(' ')[1])
      # number of lines vyasa has to write
      # before having fist cup of coffe
      v = binarySearch(n,k)
      print(v)

  in_file.close()
main()
