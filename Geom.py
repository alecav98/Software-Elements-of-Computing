#  File: Geom.py

#  Description: In this program we will create point, circle, and rectangle objects.
#  Then we will inspect their characteristics and compare each object against
#  another of the same object.

#  Student Name: Jorge Caviedes

#  Student UT EID: jac9773

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/16/2018

#  Date Last Modified: 9/17/2018

import math

class Point (object):
  # constructor
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  # the only argument c is a Circle object
  # returns a boolean
  def does_intersect (self, c):
    distance = self.center.dist (c.center)
    return ((distance - c.radius) < self.radius and (distance + c.radius) > self.radius)

  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribes (self, r):
    x_cen = (r.lr.x + r.ul.x)/2
    y_cen = (r.ul.y + r.lr.y)/2
    self.center = Point (x_cen, y_cen)
    self.radius = self.center.dist(r.ul)
    circ = Circle (self.radius, x_cen, y_cen)
    return circ

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return '(Center = ' + str(self.center) + ', radius = ' + str(self.radius) + ')'

  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs (self.radius - other.radius) < tol)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
      return float(self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
      return float(self.ul.y - self.lr.y)

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
      return float((self.length() * 2) + (self.width() * 2))

  # determine the area
  # takes no arguments, returns a float
  def area (self):
      return float(self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
      return (p.x > self.ul.x and p.x < self.lr.x and p.y > self.lr.y and p.y < self.ul.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
      if self.area() <= r.area():
          return False
      elif self.ul.y > r.ul.y and self.lr.y < r.lr.y and self.ul.x < r.ul.x and self.lr.x > r.lr.x:
          return True
      else:
          return False

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def does_intersect (self, r):
      if self.ul.x > r.lr.x or self.lr.x < self.ul.x or self.lr.y > r.ul.y or self.ul.y < r.lr.y:
          return False
      else:
          return True

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rect_circumscribe (self, c):
      self.ul_y = c.center.y + c.radius
      self.lr_y = c.center.y - c.radius
      self.ul_x = c.center.x - c.radius
      self.lr_x = c.center.x + c.radius
      rectangle = Rectangle (self.ul_x, self.ul_y, self.lr_x, self.lr_y)
      return rectangle

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
      return '(Upper left: ' + str(self.ul) + ', Lower right: ' + str(self.lr) + ')'

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
      return (self.length() == other.length() and self.width() == other.width())

def main():
  # open the file geom.txt
  in_file = open ("./geom.txt", "r")
  # create Point objects P and Q
  line = in_file.readline()
  P = Point (float(line.split(' ')[0]), float(line.split(' ')[1]))
  line = in_file.readline()
  Q = Point (float(line.split(' ')[0]), float(line.split(' ')[1]))

  # print the coordinates of the points P and Q
  print('Coordinates of P: {}'.format(P))
  print('Coordinates of Q: {}'.format(Q))

  # find the distance between the points P and Q
  print('Distance between P and Q: {}'.format(Point.dist (P, Q)))

  # create two Circle objects C and D
  line = in_file.readline()
  C = Circle (float(line.split(' ')[2]), float(line.split(' ')[0]), float(line.split(' ')[1]))
  line = in_file.readline()
  D = Circle (float(line.split(' ')[2]), float(line.split(' ')[0]), float(line.split(' ')[1]))

  # print C and D
  print('Circle C: {}'.format(C))
  print('Circle D: {}'.format(D))

  # compute the circumference of C
  print('Circumference of C: {}'.format(Circle.circumference (C)))
  # compute the area of D
  print('Area of D: {}'.format(Circle.area (D)))

  # determine if P is strictly inside C
  if Circle.point_inside (C,P) == True:
      print('P is inside C')
  else:
      print('P is not inside C')

  # determine if C is strictly inside D
  if Circle.circle_inside (D, C) == True:
      print('C is inside D')
  else:
      print('C is not inside D')

  # determine if C and D intersect (non zero area of intersection)
  if Circle.does_intersect (C, D) == True:
      print('C does intersect D')
  else:
      print('C does not intersect D')

  # determine if C and D are equal (have the same radius)
  if Circle.__eq__ (C, D) == True:
      print('C is equal to D')
  else:
      print('C is not equal to D')

  # create two rectangle objects G and H
  line = in_file.readline()
  G = Rectangle (float(line.split(' ')[0]), float(line.split(' ')[1]), float(line.split(' ')[2]), float(line.split(' ')[3]))
  line = in_file.readline()
  H = Rectangle (float(line.split(' ')[0]), float(line.split(' ')[1]), float(line.split(' ')[2]), float(line.split(' ')[3]))

  # print the two rectangles G and H
  print('Rectangle G: {}'.format(G))
  print('Rectangle H: {}'.format(H))

  # determine the length of G (distance along x axis)
  print('Length of G: {}'.format(Rectangle.length (G)))
  # determine the width of H (distance along y axis)
  print('Width of H: {}'.format(Rectangle.width (H)))
  # determine the perimeter of G
  print('Perimeter of G: {}'.format(Rectangle.perimeter (G)))
  # determine the area of H
  print('Area of H: {}'.format(Rectangle.area (H)))
  # determine if point P is strictly inside rectangle G
  if Rectangle.point_inside (G, P) == True:
      print('P is inside G')
  else:
      print('P is not inside G')

  # determine if rectangle G is strictly inside rectangle H
  if Rectangle.rectangle_inside (H, G) == True:
      print('G is inside H')
  else:
      print('G is not inside H')

  # determine if rectangles G and H overlap (non-zero area of overlap)
  if Rectangle.does_intersect (G, H) == True:
      print('G does overlap H')
  else:
      print('G does not overlap H')

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  circle_g = C.circle_circumscribes (G)
  print('Circle that circumscribes G: {}'.format(circle_g))

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  rectangle_d = Rectangle.rect_circumscribe(G,D) #G.rect_circumscribe (D)
  print('Rectangle that circumscribes D: {}'.format(rectangle_d))

  # determine if the two rectangles have the same length and width
  if  Rectangle.__eq__ (G, H) == True:
      print('Rectangle G is equal to H')
  else:
      print('Rectangle G is not equal to H')

  # close the file geom.txt
  in_file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
