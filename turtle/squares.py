import turtle

squares=8
angle = 180 - 180*(squares-2)/squares


turtle.begin_fill() # Begin the fill process.
turtle.down() # "Pen" down?
for i in range(squares):  # For each edge of the shape
    turtle.forward(40) # Move forward 40 units
    turtle.left(angle) # Turn ready for the next edge
turtle.up() # Pen up
turtle.end_fill() # End fill.

turtle.done()