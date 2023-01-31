import sys
from random import randint
from fltk import *

# Size of the window
WIDTH = 600
HEIGHT = 600

# Initial triangle vertices
A = (0, 0)
B = (WIDTH, 0)
C = (WIDTH / 2, HEIGHT)

# Draw the initial triangle
fl_begin_polygon()
fl_vertex(A[0], A[1])
fl_vertex(B[0], B[1])
fl_vertex(C[0], C[1])
fl_end_polygon()

# Function to draw the Sierpinski triangle
def sierpinski(triangle, depth):
  # Stop recursion when the desired depth is reached
  if depth == 0:
    return

  # Split the triangle into three smaller triangles
  # by connecting the midpoints of its sides
  a = midpoint(triangle[0], triangle[1])
  b = midpoint(triangle[1], triangle[2])
  c = midpoint(triangle[2], triangle[0])

  # Draw the three smaller triangles
  sierpinski((triangle[0], a, c), depth - 1)
  sierpinski((triangle[1], b, a), depth - 1)
  sierpinski((triangle[2], c, b), depth - 1)

# Function to compute the midpoint of two points
def midpoint(p1, p2):
  x = (p1[0] + p2[0]) / 2
  y = (p1[1] + p2[1]) / 2
  return (x, y)

# Create the window
win = Fl_Window(WIDTH, HEIGHT)
win.label("Sierpinski Triangle")

# Set the window color to white
win.color(FL_WHITE)

# Convert the initial triangle vertices to a list
triangle = list((A, B, C))

# Set the callback function to draw the Sierpinski triangle
win.callback(sierpinski, triangle, 7)

win.show()
Fl.run()
