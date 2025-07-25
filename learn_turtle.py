from turtle import *

# Create a turtle object (optional, or use the default)
t = Turtle()

# Set curser shape
t.shape("turtle")

# Draw a rectangle
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

# Clear drawing
t.clear()

# Draw a Square
for i in range (4):
    t.forward(100)
    t.right(90)

t.forward(100)

# Clear and reset turtle position
t.reset()

# Set fill colour
t.fillcolor("purple")

# Draw and fill a circle
t.begin_fill()
t.circle(50)
t.end_fill()

## Challenge to draw a house
t.reset()
# House body

# Reset turtle

# Roof


# Finish drawing but keep window open
done()

"""
## Other Commands
penup() or pu(): Lift the pen (no drawing).
pendown() or pd(): Lower the pen (draw).
goto(x, y): Move to position (x, y).
color("red"): Change pen color.
pensize(5): Change pen thickness.
speed(1-10): Set turtle speed.
"""

