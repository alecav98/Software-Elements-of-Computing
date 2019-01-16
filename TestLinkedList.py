#  Description: In this assignment you will be writing helper methods for
#  the LinkedList class that we developed and test them

class Link (object):
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__(self):
    self.first = None

  # get number of links
  def get_num_links (self):
    num_links = 0
    one = self.first

    # If list is empty, return 0
    if (one == None):
      return 0

    while (one != None):
      num_links += 1
      one = one.next

    return num_links

  # add an item at the beginning of the list
  def insert_first (self, data):
    new_link = Link(data)
    new_link.next = self.first
    self.first = new_link
    return

  # add an item at the end of a list
  def insert_last (self, data):
    new_link = Link(data)
    current = self.first

    # If list is empty, make link the head link
    if (current == None):
      self.first = new_link
      return
    while (current.next != None):
      current = current.next

    current.next = new_link
    return

  # add an item in an ordered list in ascending order
  def insert_in_order (self, data):
    new_link = Link(data)
    current = self.first

    # If list is empty, simply insert link
    if (current == None):
      next_link = None
      self.first = new_link
      next_link = new_link.next
      return
    next_link = self.first.next
    # If new_link is less than the first link, make new_link the first link
    if (new_link.data < current.data):
      new_link.next = current
      self.first = new_link
      return

    # If new_link is greater than first link but less than second link,
    # insert it in the middle of the first and second links
    if (next_link != None) and (new_link.data > current.data) and (new_link.data < next_link.data):
      new_link.next = current.next
      current.next = new_link
      return

    while (next_link != None) and (next_link.data < new_link.data):
      current = current.next
      next_link = current.next

    # If new_link is greater than all links in list, insert it at the end
    if (next_link == None):
      current.next = new_link
      new_link.next = None
      return

    if (next_link.data >= new_link.data):
      new_link.next = current.next
      current.next = new_link

    return

  # search in an unordered list, return None if not found
  def find_unordered (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, data):
    current = self.first

    if (current == None):
      return None       

    while (current != None) and (current.data <= data):
      if (current.data == data):
        return current
      current = current.next

    return None

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, data):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    counter = 0

    if (current == None):
      return 'None'
    line = ''
    while (current.next != None):
      line += (str(current.data) + '  ')
      current = current.next
      counter += 1
      if (counter%10 == 0):
        line += '\n'
    line += (str(current.data) + '  ')
    return line


  # Copy the contents of a list and return new list
  def copy_list (self):
    list_copy = LinkedList()

    head_copy = list_copy.first
    one = self.first

    if (one == None):
      return list_copy

    while (one != None):
      if (head_copy == None):
        new_link = one.data
        list_copy.insert_last(new_link)
        one = one.next
      else:
        new_link = one.data
        list_copy.insert_last(new_link)
        one = one.next

    list_copy.next = None

    return list_copy

  # Reverse the contents of a list and return new list
  def reverse_list (self):
    new_list = LinkedList()

    head_new = new_list.first
    one = self.first

    if (one == None):
      return new_list

    while (one != None):
      new_link = one.data
      new_list.insert_first(new_link)
      one = one.next

    return new_list

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
    new_list = LinkedList()

    head_new = new_list.first
    one = self.first

    if (one == None):
      return list_copy

    while (one != None):
      new_link = one.data
      new_list.insert_in_order(new_link)
      one = one.next

    return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    one = self.first
    if (one == None):
      True

    two = self.first.next
    while (two != None) and (one.data <= two.data):
      one = one.next
      two = two.next

    if (two == None):
      return True

    if (one.data > two.data):
      return False

  # Return True if a list is empty or False otherwise
  def is_empty (self):
    one = self.first
    if (one == None):
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
    new_list = LinkedList()

    # Create head nodes for all three lists
    new_first = new_list.first
    one_first = self.first
    other_first = other.first

    # Check if both lists are empty
    if (one_first == None) and (other_first == None):
      return new_list

    # Check if one list is empty
    if (one_first == None) or (other_first == None):
      if (one_first == None):
        return other
      else:
        return self

    # Traverse through both lists comparing their correspoding links,
    # whichever link has the greater value gets added to the new_list
    while (one_first != None) and (other_first != None):
      if (one_first.data <= other_first.data):
        new_list.insert_last(one_first.data)
        one_first = one_first.next
      else:
        new_list.insert_last(other_first.data)
        other_first = other_first.next

    if (one_first == None) or (other_first == None):
      if (one_first == None):
        while (other_first != None):
          new_list.insert_last(other_first.data)
          other_first = other_first.next
      else:
        while (one_first != None):
          new_list.insert_last(one_first.data)
          one_first = one_first.next

    return new_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    list1_counter = self.first
    list2_counter = other.first

    # If both lists are empty, return True
    if (list1_counter == None) and (list2_counter == None):
      return True

    # If one list is empty, and the other isn't: return False
    if ((list1_counter == None) and (list2_counter != None)) or ((list1_counter != None) and (list2_counter == None)):
      return False

    # Compare each link in one list to corresponding link in the other list
    while (list1_counter != None) and (list2_counter != None):
      if (list1_counter.data != list2_counter.data):
        return False
      list1_counter = list1_counter.next
      list2_counter = list2_counter.next

    # If you have reached the end of both lists, return True, else return False
    if (list1_counter == None) and (list2_counter == None):
      return True
    else:
      return False

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    # Create new linked list and new empty set
    new_list = LinkedList()
    new_set = set()

    one = self.first

    # Check if original list is empty
    if (one == None):
      return new_list

    # Traverse list and append link to new list iff that is the first appearance
    # of that link in the original list
    while (one != None):
      if (one.data in new_set):
        one = one.next
      else:
        new_list.insert_last(one.data) 
        new_set.add(one.data)                     
        one = one.next

    return new_list

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  test_list = LinkedList()
  for i in range(11):
    test_list.insert_first(i)
  print(test_list) # Should print 10  9  8  7  6  5  4  3  2  1 0

  # Test method insert_last()
  test_list1 = LinkedList()
  L = [2,3,5,7,9,1]
  for i in range(len(L)):
    test_list1.insert_last(L[i])

  print()
  print(test_list1) # Should print 2  3  5  7  9  1

  # Test method insert_in_order()
  test_list2 = LinkedList()
  L2 = [1,4,2,30,2,7,11,5,13]
  for i in range(len(L2)):
    test_list2.insert_in_order(L2[i])
  print()
  print(test_list2) # Should print 1  2  2  4  5  7  11  13  30

  # Test method get_num_links()
  print()
  print(test_list2.get_num_links()) # Should print 9
  test_list3 = LinkedList()
  print(test_list3.get_num_links()) # Should print 0

  # Test method find_unordered()
  # Consider two cases - data is there, data is not there
  test_list4 = LinkedList()
  L3 = [1,9,3,8,20,38,0,13,2,7]
  for i in range(len(L3)):
    test_list4.insert_last(L3[i])

  print()
  print(test_list4.find_unordered(38).data) # Should print out 38
  print(test_list4.find_unordered(100)) # Should print out None

  # Test method find_ordered()
  # Consider two cases - data is there, data is not there
  test_list5 = LinkedList()
  L4 = [2,4,7,10,13,20,22,23]
  for i in range(len(L4)):
    test_list5.insert_last(L4[i])

  print()
  print(test_list5.find_ordered(13).data) # Should print out 13
  print(test_list5.find_ordered(3)) # Should print out None

  # Test method delete_link()
  # Consider two cases - data is there, data is not there
  test_list6 = LinkedList()
  L4 = [2,4,7,10,13,20,22,23]
  for i in range(len(L4)):
    test_list6.insert_last(L4[i])

  print()
  print(test_list6.delete_link(22).data) # Should print out 22
  print(test_list6.delete_link(15)) # Should print out None

  # Test method copy_list()
  test_list7 = LinkedList()
  L5 = [2,4,7,10,13,20,22,23,1,42]
  for i in range(len(L5)):
    test_list7.insert_last(L5[i])

  print('\nOriginal list: {}'.format(test_list7)) # Should print out 2  4  7  10  13  20  22  23  1  42
  new_list = test_list7.copy_list()
  print('Copied list: {}'.format(new_list)) # Should print out 2  4  7  10  13  20  22  23  1  42
  print('Original list again: {}'.format(test_list7)) # Should print out 2  4  7  10  13  20  22  23  1  42

  # Test method reverse_list()
  test_list8 = LinkedList()
  L6 = [2,4,7,10,13,20,22]
  for i in range(len(L6)):
    test_list8.insert_last(L6[i])

  print('\nOriginal List: {}'.format(test_list8)) # Should print out  2  4  7  10  13  20  22
  rev_list = test_list8.reverse_list()
  print('Reversed list: {}'.format(rev_list)) # Should print out 22  20  13  10  7  4  2

  # Test method sort_list()
  test_list9 = LinkedList()
  L7 = [1,5,7,9,2,8,4,0,3,6,10]
  for i in range(len(L7)):
    test_list9.insert_last(L7[i])

  print('\nOriginal List: {}'.format(test_list9)) # Should print out 1  5  7  9  2  8  4  0  3  6  10
  print('Sorted list: {}'.format(test_list9.sort_list())) # Should print out 0  1  2  3  4  5  6  7  8  9  10

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  test_list10 = LinkedList()
  L8 = [1,5,2,7,3,57,3]
  for i in range(len(L8)):
    test_list10.insert_last(L8[i])

  print()
  print(test_list10)
  print('Is list above sorted: {}'.format(test_list10.is_sorted())) # Should print out False
  new_list10 = test_list10.sort_list()
  print(new_list10)
  print('Is list above sorted: {}'.format(new_list10.is_sorted())) # Should print out True

  # Test method is_empty()
  tl_1 = LinkedList()
  print()
  print('Linked list is: {}'.format(tl_1))
  print('Is linked list empty: {}'.format(tl_1.is_empty())) # Should print out True

  new_array = [1,2,3,4,5]
  for i in range(len(new_array)):
    tl_1.insert_last(i)
  print('\nLinked list is: {}'.format(tl_1))
  print('Is Linked List empty: {}'.format(tl_1.is_empty())) # Should print out False

  # Test method merge_list()
  merge1 = LinkedList()
  array1 = [1,5,6]
  for i in range(len(array1)):
    merge1.insert_last(array1[i])
  print()
  print('First Linked List: {}'.format(merge1))

  merge2 = LinkedList()
  array2 = [2,3,4]
  for i in range(len(array2)):
    merge2.insert_last(array2[i])
  print('Second Linked List: {}'.format(merge2))
  print('Two lists merged and sorted in ascending order: {}'.format(merge1.merge_list(merge2))) # Should print 1  2  3  4  5  6

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  le1 = LinkedList()
  le2 = LinkedList()
  arr1 = [1,2,3,100,3]
  for i in range(len(arr1)):
    le1.insert_last(arr1[i])
    le2.insert_last(arr1[i])
  print()
  print('List 1: {}'.format(le1))
  print('List 2: {}'.format(le2))
  print('Are lists equal: {}'.format(le1.is_equal(le2))) # Should print True

  le3 = LinkedList()
  arr2 = [1,2,5,100,3]
  for i in range(len(arr2)):
    le3.insert_last(arr2[i])

  print('\nList 1: {}'.format(le1))
  print('List 3: {}'.format(le3))
  print('Are lists equal: {}'.format(le1.is_equal(le3))) # Should print False

  # Test remove_duplicates()
  dupl_list = LinkedList()
  dl = [1,1,2,2,3,5,6,6]
  for i in range(len(dl)):
    dupl_list.insert_last(dl[i])
  print('\nOriginal List: {}'.format(dupl_list))
  print('Removing duplicates: {}'.format(dupl_list.remove_duplicates())) # Should print out 1  2  3  5  6


if __name__ == "__main__":
  main()
