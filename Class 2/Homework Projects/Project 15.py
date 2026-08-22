import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightskyblue")

# Create the turtle
t = turtle.Turtle()
t.speed(2)

# Draw the square
t.fillcolor("aquamarine")
t.begin_fill()

for i in range(4):
    t.forward(200)
    t.right(90)

t.end_fill()

turtle.done()