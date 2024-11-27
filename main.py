

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

# Bouncing:
#   when bouncing against the sides and top, invert angle
#   when bouncing against blocks invert the angle
#   When bouncing against bar define a function to increase inverted angle

# Create a grid to define the zones of each block to erase them on bounce, and to know the interception between ball and sides and top


import turtle
from tkinter import messagebox
import datetime as dt


# DEFINITIONS:
# Bar definitions
BAR_X = 160
BAR_Y = 10
BAR_COLOUR = 'blue'
BAR_STEP = 10

# Blocks definitions
BLOCK_X = 80
BLOCK_Y = 30
BLOCK_COLOUR_1 = 'green'
BLOCK_COLOUR_EDGE_1 = 'light green'
BLOCK_COLOUR_2 = 'dark orange'
BLOCK_COLOUR_EDGE_2 = 'orange'
BLOCK_COLOUR_3 = 'firebrick'
BLOCK_COLOUR_EDGE_3 = 'indian red'

# Ball definition
BALL_COLOUR = 'red'
BALL_RADIUS = 10

# Screen size
WIDTH = 800
HEIGHT = 600

LEFT_EDGE = -WIDTH/2
RIGHT_EDGE = WIDTH/2
TOP_EDGE = HEIGHT/2
BOTTOM_EDGE = -HEIGHT/2


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


def draw_ball(ball_radius, ball_colour, my_turtle):
    my_turtle.color(ball_colour)
    my_turtle.begin_fill()
    my_turtle.circle(radius=-ball_radius)
    my_turtle.end_fill()
    return


# Define the functions to execute when the arrow keys are pressed
def move_left():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() >= (-(WIDTH/2)):
        my_turtle.setx(my_turtle.xcor() - BAR_STEP)  # Move the turtle 20 units to the left
        my_turtle.clear()
        draw_rectangle(BAR_X, BAR_Y, BAR_COLOUR, my_turtle)
        screen.update()
    enable_key_listening()
    return


def move_right():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() < ((WIDTH/2) - BAR_X):
        my_turtle.setx(my_turtle.xcor() + BAR_STEP)  # Move the turtle 20 units to the right
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


def move_ball(my_turtle, my_angle):
    # Set up my turtle to draw the new ball
    my_turtle.penup()
    my_turtle.setheading(my_angle)
    my_turtle.forward(5)
    my_turtle.pendown()
    # Delete the last draw of the ball
    my_turtle.clear()
    # Draw new ball in new position
    draw_ball(BALL_RADIUS, BALL_COLOUR, my_turtle)
    screen.update()

    return


def check_restrictions(my_turtle, my_angle, my_lives):
    # Check laterals
    if (my_turtle.xcor() - (BALL_RADIUS / 2)) <= LEFT_EDGE:
        if 90 < my_angle < 180:
            reflected_angle = 180 - my_angle
            return reflected_angle, my_lives
        elif 180 < my_angle < 270:
            reflected_angle = 180 - my_angle + 360
            return reflected_angle, my_lives
        return my_angle, my_lives

    if (my_turtle.xcor() + (BALL_RADIUS / 2)) >= RIGHT_EDGE:
        if 0 < my_angle < 90:
            reflected_angle = 180 - my_angle
            return reflected_angle, my_lives
        elif 270 < my_angle < 360:
            reflected_angle = 540 - my_angle
            return reflected_angle, my_lives
        return my_angle, my_lives

    if (my_turtle.ycor() + BALL_RADIUS) >= TOP_EDGE:
        my_angle = 360 - my_angle
        return my_angle, my_lives

    if (my_turtle.ycor() - BALL_RADIUS) <= BOTTOM_EDGE:
        # my_angle = 360 - my_angle
        my_lives -= 1

        if my_lives < 0:
            messagebox.showinfo("You lost", "You run out of lives. Try again.")
            # Restart the game initial conditions to play a new game
            quit()

        # Print lives remaining
        lives_turtle.clear()
        lives_turtle.write(f"Lives: {my_lives}", align="center", font=("Arial", 16, "normal"))

        my_angle = 30
        ball_turtle.clear()
        bar_turtle.clear()
        initial_draw_ball()
        initial_draw_bar()


        return my_angle, my_lives

    # Check blocks: goes through all the block columns to check the height to see if the ball is in contact with
    # one of the blocks
    for j in range(11):
        if vertical_edges[j] < (my_turtle.xcor() + (BALL_RADIUS / 2)) <= vertical_edges[(j + 1)]:
            # Checks green blocks
            if (horizontal_edges[0] < my_turtle.ycor() < horizontal_edges[1]) and (block_turtle_green[j] != ""):
                block_turtle_green[j].clear()   # if the ball is hitting the j-green-block it gets cleared
                block_turtle_green[j] = ""  # The associated turtle is replaced with "" to check the winning condition
                my_angle = 360 - my_angle
                return my_angle, my_lives
            # Checks orange blocks
            if (horizontal_edges[1] < my_turtle.ycor() < horizontal_edges[2]) and (block_turtle_orange[j] != ""):
                block_turtle_orange[j].clear()
                block_turtle_orange[j] = ""
                my_angle = 360 - my_angle
                return my_angle, my_lives
            # Checks red blocks
            if (horizontal_edges[2] < my_turtle.ycor() < horizontal_edges[3]) and (block_turtle_red[j] != ""):
                block_turtle_red[j].clear()
                block_turtle_red[j] = ""
                my_angle = 360 - my_angle
                return my_angle, my_lives

    # Check bar:
    if bar_turtle.ycor() <= my_turtle.ycor() <= (bar_turtle.ycor() + BALL_RADIUS):
        if bar_turtle.xcor() <= my_turtle.xcor() < (bar_turtle.xcor() + (BAR_X/3)):
            my_angle = 360 - my_angle
            return my_angle, my_lives
        if bar_turtle.xcor() + (BAR_X/3) <= my_turtle.xcor() <= (bar_turtle.xcor() + (BAR_X * 2/3)):
            my_angle = 360 - my_angle
            return my_angle, my_lives
        if bar_turtle.xcor() + (BAR_X * 2/3) < my_turtle.xcor() <= (bar_turtle.xcor() + BAR_X):
            my_angle = 360 - my_angle
            return my_angle, my_lives

    return my_angle, my_lives


def verify_winning():
    are_all_empty = all(element == "" for element in block_turtle_green) and \
                    all(element == "" for element in block_turtle_orange) and \
                    all(element == "" for element in block_turtle_red)
    return are_all_empty


def delay(milliseconds):
    target_time = dt.datetime.now() + dt.timedelta(milliseconds=milliseconds)
    while dt.datetime.now() < target_time:
        pass
    return


def initial_draw_bar():
    # DRAWING
    # Draw the bar in the starting position
    turtle_move(-(BAR_X / 2), -((HEIGHT / 2) - 60), bar_turtle)
    draw_rectangle(BAR_X, BAR_Y, BAR_COLOUR, bar_turtle)
    screen.update()
    return


def draw_blocks():
    for i in range(10):
        turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 0, block_turtle_green[i])
        draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_1, block_turtle_green[i])

        turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 34, block_turtle_orange[i])
        draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_2, block_turtle_orange[i])

        turtle_move(-(WIDTH / 2) + (i * BLOCK_X), 68, block_turtle_red[i])
        draw_rectangle(BLOCK_X, BLOCK_Y, BLOCK_COLOUR_3, block_turtle_red[i])
    return


def initial_draw_ball():
    turtle_move(0, -((HEIGHT / 2) - 80), ball_turtle)
    draw_ball(ball_radius=BALL_RADIUS, ball_colour=BALL_COLOUR, my_turtle=ball_turtle)
    ball_turtle.setheading(30)
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
# bar_turtle.hideturtle()
bar_turtle.speed(0)  # Set the turtle speed to the fastest

# Set up ball turtle
ball_turtle = turtle.Turtle()
ball_turtle.hideturtle()
ball_turtle.speed(0)

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

# Generate edges for defining zones
vertical_edges = []
horizontal_edges = []

# Vertical edges in order: v0 = -400, v1 = -320, v2 = -240, v3 = -160, v4 = -80, v5 = 0, v6 = 80, v7 = 160,
# v8 = 240, v9 = 320, v10 = 400
for i in range(11):
    vertical_edges.append(-(WIDTH / 2) + (i * BLOCK_X))
print(vertical_edges)

# Horizontal edges in order: h0 = -34, h1 = 0, h2 = 34, h3 = 68
for i in range(4):
    horizontal_edges.append(i * 34 - 34)
print(horizontal_edges)

# DRAW

# Draw the ball in the initial position
initial_draw_bar()

# Draw the blocks
draw_blocks()

# Draw the ball in initial place
initial_draw_ball()

# Lives set up
lives_turtle = turtle.Turtle()
lives_turtle.hideturtle()
# Position the turtle
lives_turtle.penup()
lives_turtle.goto((LEFT_EDGE + 50), (TOP_EDGE - 50))  # Move to a starting position
# Write the message
lives_remaining = 3
lives_turtle.write(f"Lives: {lives_remaining}", align="center", font=("Arial", 16, "normal"))


screen.update()

# Listen for left and right arrow keys
screen.listen()  # Start listening for keyboard events
screen.onkeypress(move_left, "Left")  # Bind the left arrow key to the move_left function
screen.onkeypress(move_right, "Right")  # Bind the right arrow key to the move_right function

winning = False
while not winning:
    delay(20)

    angle = ball_turtle.heading()
    # Check if the ball is overlapping with edges, top, bottom, or the bar. And modify angle accordingly.
    angle, lives_remaining = check_restrictions(my_turtle=ball_turtle, my_angle=angle, my_lives=lives_remaining)

    # Print lives remaining
    lives_turtle.clear()
    lives_turtle.write(f"Lives: {lives_remaining}", align="center", font=("Arial", 16, "normal"))

    move_ball(my_turtle=ball_turtle, my_angle=angle)
    screen.update()
    screen.ontimer(lambda: move_ball(ball_turtle, angle), 20)

    # Check if the winning condition is true
    winning = verify_winning()
    if winning is True:
        # Show winning message to the user.
        messagebox.showinfo("You won!", "Congratulations you won the game!!!")
        print(f"Winning is {winning}")
        # return  # Exits the move_ball() so the ball stops in screen

# Keep the window open
screen.mainloop()

