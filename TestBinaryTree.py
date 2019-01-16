#  Description: We will add to the classes Node and Tree and test them.

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self, tree_str):
    self.root = None

    for i in range(len(tree_str)):
      self.insert(tree_str[i])
    return

  # the insert() function adds a node containing a number in
  # the binary search tree. If the number already exists, it
  # does not add that number. There are no duplicate numbers
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
        if (ch < current.data):
          current = current.lchild
        elif (ch > current.data):
          current = current.rchild
        else:
          # Data is already a node, so do nothing
          return

      if (ch < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # pre order traversal -center, left, right
  def pre_order (self, aNode, L):
    if (aNode != None):
      L.append(aNode.data)
      self.pre_order (aNode.lchild, L)
      self.pre_order (aNode.rchild, L)

  # Returns true if two binary trees are similar, pNode is root of other tree
  def is_similar (self, pNode):
    list1 = []
    list2 = []

    # Set starting value of self Tree
    current1 = self.root

    # Set starting value of tree starting at pNode
    current2 = pNode

    # Append all the values of self Tree, in the order they were found, to a list
    self.pre_order(current1, list1)

    # Append all the values of other Tree, in the order they were found, to a list
    self.pre_order(current2, list2)

    # Compare lists
    if (len(list1) != len(list2)):
      return False
    else:
      for i in range(len(list1)):
        if (list1[i] != list2[i]):
          return False

    return True

  # Prints out all nodes at the given level
  def print_level (self, level):
    current = self.root
    sum = 0
    print('The nodes on level {} from left to right are: '.format(level))
    diff_nodes = []
    node_str = ''

    self.print_level_helper(current, level, sum, diff_nodes)

    for i in range(len(diff_nodes)):
      node_str = node_str + diff_nodes[i] + ' '
    print(node_str)

    return

  def print_level_helper(self, current, level, sum, diff_nodes):
    if (current == None):
      # if you have reached the end of that path, return
      return
    elif (sum == level):
      # If you have reached the level, append value of node to list
      diff_nodes.append(str(current.data))
    else:
      # Otherwise, increase counter and continue in both directions
      self.print_level_helper(current.lchild, level, sum+1, diff_nodes)
      self.print_level_helper(current.rchild, level, sum+1, diff_nodes)

   # Returns the height of the tree
  def get_height(self):
    position = self.root
    list_sums = []
    sum = 0

    self.get_height_helper (position, list_sums, sum)
    return max(list_sums)

  def get_height_helper(self, position, list_sums, sum):
    # If you are at a leaf node, append sum to list of sums
    if (position.lchild == None) and (position.rchild == None):
      list_sums.append(sum)
    else:
      # if still have right children, recursively keep going right
      if (position.lchild == None):
        self.get_height_helper(position.rchild, list_sums, sum+1)
      # if still have left children, recursively keep going left
      elif (position.rchild == None):
        self.get_height_helper(position.lchild, list_sums, sum+1)
       # Otherwise, keep going in both directions
      else:
        self.get_height_helper(position.rchild, list_sums, sum+1)
        self.get_height_helper(position.lchild, list_sums, sum+1)


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root (total # of nodes)
  def num_nodes (self):
    left = []
    right = []
    first = self.root
    l_root = first.lchild
    r_root = first.rchild

    # Get list of all nodes in left subtree
    self.pre_order(l_root, left)

    # Get list of all nodes in right subtree
    self.pre_order(r_root, right)

    num_left = len(left)
    num_right = len(right)

    # Get total number of nodes in Tree
    tot_nodes = num_left + num_right + 1

    return tot_nodes

def main():
    # Create three trees - two are the same and the third is different
    arr_1 = [15,13,17,16,32,54,3,4,5]
    new_tree = Tree(arr_1)
    print("Tree 1 is made up of: '{}'".format(arr_1))

    arr_2 = [15,13,17,16,32,54,3,4,5]
    new_tree2 = Tree(arr_2)
    print("Tree 2 is made up of: '{}'".format(arr_2))

    arr_3 = [15,17,13,12,16,20,14,1,2]
    new_tree3 = Tree(arr_3)
    print("Tree 3 is made up of: '{}'".format(arr_3))

    arr_4 = [5,4,6,2,8,3,7]
    n_tree = Tree(arr_4)
    print("Tree 4 is made up of: '{}'".format(arr_4))
    print()

    # Test your method is_similar()
    similar_12 = new_tree.is_similar(new_tree2.root)
    similar_23 = new_tree2.is_similar(new_tree3.root)
    similar_13 = new_tree.is_similar(new_tree3.root)

    print('Is tree 1 similar to tree 2: {}'.format(similar_12)) # Should print True
    print('Is tree 2 similar to tree 3: {}'.format(similar_23)) # Should print False
    print('Is tree 3 similar to tree 1: {}'.format(similar_13)) # Should print False
    print()

    # Print the various levels of two of the trees that are different
    print('Printing nodes for Tree 1:')
    nodes_t1 = new_tree.print_level(3) # 4 54

    print()
    print('Printing nodes for Tree 3:')
    nodes_t3 = new_tree3.print_level(1) # 13 17
    print()

    # Get the height of the two trees that are different
    h_n_height = n_tree.get_height()
    new_height = new_tree.get_height()

    print("The height of Tree 4 is: {}".format(h_n_height)) # Should print 3
    print("The height of Trees 1 and 2 is: {}".format(new_height)) # Should print 4
    print()

    # Get the total number of nodes a binary search tree
    nodes_tree_4 = n_tree.num_nodes()
    nodes_tree_1 = new_tree.num_nodes()

    print("The total number of nodes in Tree 4 are: {}".format(nodes_tree_4)) # 7
    print("The total number of nodes in Tree 1 are: {}".format(nodes_tree_1)) # 9


main()
