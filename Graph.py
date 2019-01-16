#  File: Graph.py

#  Description:

#  Student Name: Jorge Caviedes

#  Student UT EID: Jac9773

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 11/27/2018

#  Date Last Modified: 11/28/2018

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)

      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
    theQueue = Queue()
    theQueue.enqueue(v)
    (self.Vertices[v]).visited = True
    while (not theQueue.isEmpty()):
      current = theQueue.dequeue()
      print(self.Vertices[current])
      next = self.getAdjUnvisitedVertex(current)
      while (next != -1):
        theQueue.enqueue(next)
        (self.Vertices[next]).visited = True
        next = self.getAdjUnvisitedVertex(current)
    # the queue is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
    return

    '''
    #print (self.Vertices [v]) ###############################
    #theQueue.enqueue(current)
    next = self.getAdjUnvisitedVertex(self.getIndex(current.label))
    theQueue.enqueue(next)
    # visit other vertices according to breadth
    while (not theQueue.isEmpty()): #######################
      # get an adjacent unvisited vertex
      next = self.getAdjUnvisitedVertex(self.getIndex(current.label)) #########################
      if (next == -1):
        current = theQueue.dequeue()
        print(current) ######################################
      else:
        (self.Vertices[next]).visited = True
        theQueue.enqueue(next)
    '''

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    vert1_idx = self.getIndex(fromVertexLabel)
    vert2_idx = self.getIndex(toVertexLabel)
    return int(self.adjMat[vert1_idx][vert2_idx])

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    neighbor_list = []
    num_vert = len(self.Vertices)

    # Get vertex label index
    vert_idx = self.getIndex(vertexLabel)

    # If vertex doesn't exist, return empty list
    if (vert_idx == -1):
      return neighbor_list

    for i in range(num_vert):
      if (self.adjMat[i][vert_idx] == 1):
        neighbor_list.append(self.Vertices[vert_idx])

    return neighbor_list

  # get a copy of the list of vertices
  def getVertices (self):
    return self.Vertices[:]

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    v1 = self.getIndex(fromVertexLabel)
    v2 = self.getIndex(toVertexLabel)
    self.adjMat[v1][v2] = 0
    self.adjMat[v2][v1] = 0
    return

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    # get index of vertex
    v_idx = self.getIndex(vertexLabel)

    # delete vertex from vertices list
    del self.Vertices[v_idx]

    # Delete the corresponding row and column of the vertex
    for i in range(len(self.adjMat)):
      del self.adjMat[i][v_idx]
    del self.adjMat[v_idx]

    return

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)                        ############

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)                             ############
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())
  #print (numEdges)                           #############

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)                             #############
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    try:
      weight = int (edge[2])
    except:
      weight = 1

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  '''
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()
  '''
  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  #print (startVertex)                      ###############

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  #print (startIndex)                       ###############

  # test depth first search
  print ("\nDepth First Search from " + startVertex)
  cities.dfs (startIndex)

  # test breadth first search
  print ("\nBreadth First Search from " + startVertex)
  cities.bfs (startIndex)
  print()

  # test deletion of an edge
  print('Deletion of an Edge')
  edge_cities = (inFile.readline()).strip()
  edge_cities = edge_cities.split()
  cities.deleteEdge(edge_cities[0], edge_cities[1])

  # now print the adjacency matrix showing deletions
  print ("\nAdjacency Matrix")
  for i in range (len(cities.adjMat)):
    for j in range (len(cities.adjMat[i])):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # test deletion of a vertex
  print('Deletion of a vertex')
  del_vertex = (inFile.readline()).strip()
  cities.deleteVertex(del_vertex)

  # Print list of cities after deletion
  print()
  print('List of Vertices')
  for i in range(len(cities.Vertices)):
    print(cities.Vertices[i])

  # now print the adjacency matrix showing vertex deletion
  print ("\nAdjacency Matrix")
  for i in range (len(cities.adjMat)):
    for j in range(len(cities.adjMat[i])):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # close file
  inFile.close()

if __name__ == "__main__":
  main()
