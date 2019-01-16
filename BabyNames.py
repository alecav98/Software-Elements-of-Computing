#  Description: This program allows a user to query a data base of the 1000
#  most popular baby names in the United States per decade for the past 11
#  decades under certain constraints implemented below.

# This function returns True if a name exists in the dictionary and False otherwise.
# The function takes as input the data that we read in from the text file in the
# main function. This function prints out 'This name exists.' if the name is found
# in the dictionary and '(name) does not appear in any decade.' if the Name
# is not found in the dictionary.
def NameExist(data):
  strng = input('Enter a name: ')
  count = 0
  for i in data:
      if strng in data.keys():
          count += 1
          break
      else:
          count += 0
  if count > 0:
      print('This name exists.')
  else:
      print(strng + ' does not appear in any decade.')

# This function returns all the rankings for a given name. The function takes
# as input the data that we read in from the text file in the main function.
# The function will ask the user for a name and will print out all the rankings
# the name has as a string separated by spaces or will print out 'The name is
# not in the list.' if the name is not found in the list.
def ReturnRankings(data):
  name = input("Enter a name: ")
  count = 0
  for i in data:
      if name in data.keys():
          count += 1
      else:
          count += 0
  if count > 0:
      line = data[name]
      strng = ' '.join(line)
      print(name + ': ' + strng)
  else:
      print('That name is not in the list.')

# This function returns a list of names that have a rank in all the decades
# in sorted order by name. The function takes as input the data we read in
# from the text file in the main function. It then uses a nested for loop
# to find all the keys which have a rank in all the decades. The list is then
# turned into a string and printed.
def RankInAllDecades(data):
  list = []
  for key in data.keys():
      count = 0
      line = data[key]
      for i in range(len(line)):
          if line[i] == '0':
              count += 1
          else:
              pass
      if count == 0:
          list.append(key)
      else:
          pass
  print('{} names appear in every decade. The names are:'.format(len(list)))
  list_to_print = '\n'.join(list)
  print(list_to_print)

# This function displays all the names that have a rank in a given decade in
# order of rank. The function takes as input the data we read in from the text
# file in the main function. It then uses a nested loop to find all the keys
# which have a rank for the specified decade. And finally it uses another for
# loop to print out the key value pairs sorted by rank.
def RankInDecade(data):
  num = int(input('Enter a decade: '))
  decade = (num%1900)/10
  new_rank_dict = {}
  for key in data.keys():
      line = data[key]
      for i in range(len(line)):
          if line[i] > '0' and i == decade:
              new_rank_dict[key] = int(line[i])
  print('The names are in order of rank:\n')
  for key, value in sorted(new_rank_dict.items(), key=lambda x: x[1]):      ### Dictionary sorted by value
      print('{}: {}'.format(key, value))

# This function displays all names that are getting more popular in every decade.
# The names must have a rank in all the decades to qualify and the output must
# be sorted by name. The function creates a new dictionary which contains only
# those key-value pairs for which the value has a rank in every decade. Then, it
# uses a nested for loop to find keys which have a decreasing (better) ranking
# every decade than the one before. Finally, it uses a for loop to print out
# the results.
def Popular(data):
  new_dict = {}
  for key in data.keys():
      count = 0
      line = data[key]
      for i in range(len(line)):
          if line[i] == '0':
              count += 1
          else:
              pass
      if count == 0:
          new_dict[key] = line
  popular_list = []
  for key in new_dict.keys():
      count = 0
      line = new_dict[key]
      for i in range(len(line)):
          if i == 0:
              pass
          elif i > 0 and int(line[i]) < int(line[i-1]):
              pass
          else:
              count += 1
      if count == 0:
          popular_list.append(key)
  print('{} names are more popular every decade:'.format(len(popular_list)))
  for i in range(len(popular_list)):
      print(popular_list[i])

# This function displays all names that are getting less popular in every
# decade. The names must have a rank in all the decades to qualify and the output
# must be sorted by name. The function creates a new dictionary which contains only
# those key-value pairs for which the value has a rank in every decade. Then, it
# uses a nested for loop to find keys which have a increasing (worse) ranking
# every decade than the one before. Finally, it uses a for loop to print out
# the results.
def LessPopular(data):
  new_dict = {}
  for key in data.keys():
      count = 0
      line = data[key]
      for i in range(len(line)):
          if line[i] == '0':
              count += 1
          else:
              pass
      if count == 0:
          new_dict[key] = line
  popular_list = []
  for key in new_dict.keys():
      count = 0
      line = new_dict[key]
      for i in range(len(line)):
          if i == 0:
              pass
          elif i > 0 and int(line[i]) > int(line[i-1]):
              pass
          else:
              count += 1
      if count == 0:
          popular_list.append(key)
  print('{} names are less popular every decade:'.format(len(popular_list)))
  for i in range(len(popular_list)):
      print(popular_list[i])

def main():
    while True:
        # Check that the file was read in successfully and all functions work
        try:
            data = {}
            in_file = open ("names.txt", "r")
            for line in in_file:
                line = line.strip('\n')
                key = line.split(' ')[0]
                value = line.split(' ')[1:]
                data[key] = value
            print('\nOptions:')
            print('Enter 1 to search for names.')
            print('Enter 2 to display data for one name.')
            print('Enter 3 to display all names that appear in only one decade.')
            print('Enter 4 to display all names that appear in all decades.')
            print('Enter 5 to display all names that are more popular in every decade.')
            print('Enter 6 to display all names that are less popular in every decade.')
            print('Enter 7 to quit.')
            num = int(input('\nEnter choice: '))
            if num == 1:
                NameExist(data)
                main()
            elif num == 2:
                ReturnRankings(data)
                main()
            elif num == 3:
                RankInDecade(data)
                main()
            elif num == 4:
                RankInAllDecades(data)
                main()
            elif num == 5:
                Popular(data)
                main()
            elif num == 6:
                LessPopular(data)
                main()
            elif num == 7:
                raise SystemExit
        # If file could not be read, then except will catch the error and print
        # a message to the user
        except IOError:
            print('The system could not read the file.')
        finally:
            in_file.close()
            
if __name__ == "__main__":
  main()
