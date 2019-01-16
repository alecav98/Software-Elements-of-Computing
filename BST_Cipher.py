#  Description: We will will create a simple encryption scheme using
#  a binary search tree. To encode a sentence, we insert each letter
#  into a binary tree using the ASCII value as a comparative measure.

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None

    encrypt_str = encrypt_str.strip().lower()
    for i in range(len(encrypt_str)):
      # If character is a space, enter it into the tree
      if (ord(encrypt_str[i]) == 32):
        self.insert(encrypt_str[i])
      # If character is a lowercase letter, enter it into the tree
      elif (ord(encrypt_str[i]) >= 97 and ord(encrypt_str[i]) <= 122):
        self.insert(encrypt_str[i])
      else:
        # Otherwise ignore character
        pass

    return

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new_node = Node (ch)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (ord(ch) < ord(current.data)):
          current = current.lchild
        elif (ord(ch) > ord(current.data)):
          current = current.rchild
        else:
          # Data is already a node, so do nothing
          return

      if (ord(ch) < ord(parent.data)):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    current = self.root
    lr_str = ''

    # If data is the root node, return '*'
    if (current.data == ch):
      return '*'

    # while ord(letter) is less/greater than the current node, go left/right
    while (current != None) and (current.data != ch):
      if (ord(ch) < ord(current.data)):
        current = current.lchild
        lr_str += '<'
      else:
        current = current.rchild
        lr_str +='>'

    # If node doesn't exist, return empty string
    if (current == None):
      return ''
    else:
      return lr_str

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    for i in range(len(st)):
      if (st[i] == '<'):
        current = current.lchild
      elif (st[i] == '>'):
        current = current.rchild

    if (current == None):
      return ''
    else:
      return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    new_string = st.lower()
    encrypted_str = ''
    for i in range(len(new_string)):
      direction_str = self.search(new_string[i])
      if (direction_str == ''):
        pass
      elif (direction_str != '') and (i != len(new_string)-1):
        encrypted_str += self.search(new_string[i]) + '!'
      elif (direction_str != '') and (i == len(new_string)-1):
        encrypted_str += self.search(new_string[i])

    return encrypted_str

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    dec_str = ''
    part_str = ''
    current = self.root

    i = 0
    while (i < len(st)):
      if (st[i] != '!') :
        part_str += st[i]
        i = i+1
      else:
        dec_str += self.traverse(part_str)
        part_str = ''
        i = i+1

    dec_str += self.traverse(part_str)
    return dec_str

def main():
  # Ask the user for the pass key
  pass_key = input('Enter encryption key: ')

  # Create the Binary Tree
  new_tree = Tree(pass_key)

  # Ask for sentence to be encrypted, print encrypted version
  plain1 = input('Enter string to be encrypted: ')
  encrypted1 = new_tree.encrypt(plain1)
  print('Encrypted string: {}'.format(encrypted1))
  print()

  # Ask for sentence to be decrypted, print decrypted version
  encrypted2 = input('Enter string to be decrypted: ')
  plain2 = new_tree.decrypt(encrypted2)
  print('Decrypted string: {}'.format(plain2))

main()
