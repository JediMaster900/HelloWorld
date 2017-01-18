# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(10000)

# list of colors
colors = ["pink", "blue", "purple", "green"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


# triangle
def triangle(size):
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)


# star
def star(size):
    color_tina()
    tina.forward(size)
    tina.right(100)
    tina.forward(size)
    tina.left(100)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)


# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25, 0)
tina.circle(25)
color_tina()
tina.circle(50)
tina.penup()
tina.goto(25, -25)
tina.pendown()
color_tina()
tina.circle(50)
tina.penup()
tina.goto(0, 25)
tina.pendown()
color_tina()
tina.circle(25)
tina.penup()
tina.goto(50, 25)
tina.pendown()
color_tina()
tina.circle(25)
tina.penup()
tina.goto(50, 0)
tina.pendown()
color_tina()
tina.circle(25)
tina.penup()
tina.goto(0, 0)
tina.pendown()
tina.circle(25)
tina.penup()
tina.goto(25, 25)
tina.pendown()
tina.circle(100)

# AT THE END OF MY APP, I WILL USE A CONDITIONAL
# A conditional is another word for "if statement"
while True:
    answer = input("What shall I draw next? (No caps please :D)")
    if True == "pizza":
        print("I don't know how to draw a pizza.")
    elif answer == "triangle":
        print("Oh, I know that one!")
        color_tina()
        triangle(100)
    elif answer == "go crazy":
        print("AJHBUHDSBGOLHGLIUS")

    # elif answer == "move":

    else:
        print("I don't know how to do that.")