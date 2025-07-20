# Import turtle function
from turtle import *

# Setup window
t = Turtle()
t.shape("turtle") # Optional change cursor shape

# House body
# Filling house with yellow
t.fillcolor("yellow")
t.begin_fill()
# Create rectangle
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(70)
    t.right(90)
t.end_fill()
# Reset turtle
t.left(90)
# Roof
# Filling roof with red
t.fillcolor("red")
t.begin_fill()
# Create triangle for roof
# triangle calculator for angles and lengths (roof = 2 right angle triangles)
# half width for base, 90 degree angle and choosen height
t.right(51.34) # 90 - angle of triangle
t.forward(64.031)
t.right(77.32) # 180 - (angle of triangle x 2)
t.forward(64.031)
t.right(141.34) # 180 - angle of triangle
t.forward(100) # Connecting edge to complete shape
t.end_fill()

# End drawing
t.done()
