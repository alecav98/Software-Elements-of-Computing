#  Description: The program will print out the order in which
#  the soldiers get eliminated in the famous Josephus problem.

class Link(object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class CircularList(object):
  # Constructor
  def __init__ ( self ):
    self.first = None

  # Insert an element (value) in the list
  def insert (self, data):
    new_link = Link(data)
    current = self.first

    # If list is empty, make link the head link
    if (current == None):
      self.first = new_link
      new_link.next = new_link
      return

    # Traverse through list until you get to the last element
    while (current.next != self.first):
      current = current.next

    current.next = new_link
    new_link.next = self.first   #This Makes list circular
    return

  # Find the link with the given data (value)
  def find ( self, data ):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      current = current.next

    return current

  # Delete a link with a given data (value)
  def delete ( self, data ):
    previous = self.first
    current = self.first.next

    if (current == None) and (previous.data != data):
      return None

    if (previous.data == data) and (current != None):
      self.first = current

    while (current.data != data):
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    print(current.data)
    return current

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after ( self, start, n ):
    start_link = self.find(start)

    for i in range(n-2):
      start_link = start_link.next

    start_link = start_link.next
    temp = start_link.next
    self.delete(start_link.data)

    return temp

  # Return a string representation of a Circular List
  def __str__ ( self ):
    pass

def main():
  # First we must open and read the file
  in_file = open("./josephus.txt", "r")

  # read first line
  line = in_file.readline()
  line = line.strip()
  num_soldiers = int(line)

  # Create circular list with number of soldiers specified
  circ_list = CircularList()
  for i in range(num_soldiers):
    circ_list.insert(i+1)

  # Read second line, tells where the counting starts
  line2 = in_file.readline()
  n = line2.strip()
  start_soldier = int(n)

  # Read third line, tells us elimination number
  line3 = in_file.readline()
  number = line3.strip()
  e_num = int(number)

  # Start deleting soldiers
  for i in range(num_soldiers):
    new_start = circ_list.delete_after(start_soldier, e_num)
    start_soldier = new_start.data

main()
