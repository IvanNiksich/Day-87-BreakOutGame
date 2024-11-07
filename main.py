

# Game mechanics:

# Wall of bricks:
#   start with 4 lines of bricks, length of bricks to be determined
#   when the ball touches the edge of a brick, the brick is destroyed and the ball bounces in a reflected angle
#


# Bar:
#   when the ball touches the edge of the bar, it bounces in a angle that varies with the distance to the middle of the bar
#   the bar moves with the keyword.

# Ball:
#   The ball speed increments with score.


# Score:
#   Score increments with bricks destroyed.

# Lives:
#   There are a number of predefined numbers.
#   Every time the ball gets down the line of the bar the player looses a life.


import turtle

# Bar definitions
BAR_X = 160
BAR_Y = 10
BAR_COLOUR = 'blue'

# Blocks definitions
BLOCK_X = 80
BLOCK_Y = 30
BLOCK_COLOUR_1 = 'green'
BLOCK_COLOUR_EDGE_1 = 'light green'
BLOCK_COLOUR_2 = 'dark orange'
BLOCK_COLOUR_EDGE_2 = 'orange'
BLOCK_COLOUR_3 = 'firebrick'
BLOCK_COLOUR_EDGE_3 = 'indian red'

# Screen size
WIDTH = 800
HEIGHT = 600


def turtle_move(x_pos, y_pos, my_turtle):
    # Move the turtle to a new position without drawing
    my_turtle.penup()  # Lift the pen
    my_turtle.goto(x_pos, y_pos)  # Move to (x, y)
    my_turtle.pendown()  # Lower the pen to start drawing
    return


# Function to draw a rectangle
def draw_rectangle(rectangle_width, rectangle_height, rectangle_colour, my_turtle):
    for _ in range(2):
        my_turtle.fillcolor(rectangle_colour)  # Set the fill color to blue
        my_turtle.begin_fill()  # Begin filling the shape
        my_turtle.forward(rectangle_width)  # Draw the width
        my_turtle.right(90)    # Turn right
        my_turtle.forward(rectangle_height)    # Draw the height
        my_turtle.right(90)    # Turn right
        my_turtle.end_fill()    # End filling the shape
    return


# Define the functions to execute when the arrow keys are pressed
def move_left():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() >= (-(WIDTH/2)):
        my_turtle.setx(my_turtle.xcor() - 20)  # Move the turtle 20 units to the left
        my_turtle.clear()
        draw_rectangle(BAR_X, BAR_Y, BAR_COLOUR, my_turtle)
        screen.update()
    enable_key_listening()
    return


def move_right():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() < ((WIDTH/2) - BAR_X):
        my_turtle.setx(my_turtle.xcor() + 20)  # Move the turtle 20 units to the right
        my_turtle.clear()
        draw_rectangle(BAR_X, BAR_Y, BAR_COLOUR, my_turtle)
        screen.update()
    enable_key_listening()
    return


# Disable listening for arrow keys
def disable_key_listening():
    screen.onkey(None, "Left")  # Disable the Left arrow key
    screen.onkey(None, "Right")  # Disable the Right arrow key
    return


# Enable listening for arrow keys again
def enable_key_listening():
    screen.onkey(move_left, "Left")  # Enable the Left arrow key
    screen.onkey(move_right, "Right")  # Enable the Right arrow key
    return


# MAIN

# Create and set up the screen
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Break Out - Classic game")
screen.tracer(0)  # Disable automatic screen updates


# Get the size of the turtle window
width = screen.window_width()
height = screen.window_height()

# Print the size of the window
print(f"Window width: {width} pixels")
print(f"Window height: {height} pixels")

# TURTLES CONFIG
# Set up the bar turtle
bar_turtle = turtle.Turtle()
bar_turtle.pensize(2)
bar_turtle.color(BAR_COLOUR)
bar_turtle.hideturtle()
bar_turtle.speed(0)  # Set the turtle speed to the fastest

# Set up block turtles
block_turtle_green = []
block_turtle_orange = []
block_turtle_red = []

for i in range(10):
    block_turtle_green.append("")
    block_turtle_orange.append("")
    block_turtle_red.append("")

for i in range(10):
    block_turtle_green[i] = turtle.Turtle()
    block_turtle_green[i].pensize(4)
    block_turtle_green[i].color(BLOCK_COLOUR_EDGE_1)
    block_turtle_green[i].hideturtle()
    block_turtle_green[i].speed(0)

    block_turtle_orange[i] = turtle.Turtle()
    block_turtle_orange[i].pensize(4)
    block_turtle_orange[i].color(BLOCK_COLOUR_EDGE_2)
    block_turtle_orange[i].hideturtle()
    block_turtle_orange[i].speed(0)

    block_turtle_red[i] = turtle.Turtle()
    block_turtle_red[i].pensize(4)
    block_turtle_red[i].color(BLOCK_COLOUR_EDGE_3)
    block_turtle_red[i].hideturtle()
    block_turtle_red[i].speed(0)

# DRAWING
# Draw the bar in the starting position
turtle_move(-(BAR_X / 2), -((HEIGHT / 2) - 60), bar_turtle)
draw_rectangle(BAR_X, BAR_Y, BAR_COLOUR, bar_turtle)
screen.update()

# Draw the blocks
for i in range(10):
    turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 0, block_turtle_green[i])
    draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_1, block_turtle_green[i])

    turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 34, block_turtle_orange[i])
    draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_2, block_turtle_orange[i])

    turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 68, block_turtle_red[i])
    draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_3, block_turtle_red[i])

screen.update()

# Listen for left and right arrow keys
screen.listen()  # Start listening for keyboard events
screen.onkeypress(move_left, "Left")  # Bind the left arrow key to the move_left function
screen.onkeypress(move_right, "Right")  # Bind the right arrow key to the move_right function

# Keep the window open
turtle.done()
