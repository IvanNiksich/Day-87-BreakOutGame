

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

# Bar size
BAR_X = 160
BAR_Y = 10

WIDTH = 800
HEIGHT = 600


def turtle_move(x_pos, y_pos, myturtle):
    # Move the turtle to a new position without drawing
    myturtle.penup()  # Lift the pen
    myturtle.goto(x_pos, y_pos)  # Move to (x, y)
    myturtle.pendown()  # Lower the pen to start drawing
    return


# Function to draw a rectangle
def draw_rectangle(rectangle_width, rectangle_height, my_turtle):
    for _ in range(2):
        my_turtle.forward(rectangle_width)  # Draw the width
        my_turtle.right(90)    # Turn right
        my_turtle.forward(rectangle_height)    # Draw the height
        my_turtle.right(90)    # Turn right


# Define the functions to execute when the arrow keys are pressed
def move_left():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() >= (-(WIDTH/2)):
        my_turtle.setx(my_turtle.xcor() - 20)  # Move the turtle 20 units to the left
        my_turtle.clear()
        draw_rectangle(BAR_X, BAR_Y, my_turtle)
        screen.update()
    enable_key_listening()
    return


def move_right():
    disable_key_listening()
    my_turtle = bar_turtle
    if my_turtle.xcor() < ((WIDTH/2) - BAR_X):
        my_turtle.setx(my_turtle.xcor() + 20)  # Move the turtle 20 units to the right
        my_turtle.clear()
        draw_rectangle(BAR_X, BAR_Y, my_turtle)
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


screen = turtle.Screen()
# Set up the screen
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Draw a 10x100 Rectangle")
screen.tracer(0)  # Disable automatic screen updates


# Get the size of the turtle window
width = screen.window_width()
height = screen.window_height()

# Print the size of the window
print(f"Window width: {width} pixels")
print(f"Window height: {height} pixels")


# Set up the turtles
bar_turtle = turtle.Turtle()
bar_turtle.pensize(2)
bar_turtle.color("blue")
bar_turtle.speed(0)  # Set the turtle speed to the fastest


# Initialize game
turtle_move(-(BAR_X / 2), -((HEIGHT / 2) - 60), bar_turtle)

# Draw a 10x100 rectangle as bar
draw_rectangle(BAR_X, BAR_Y, bar_turtle)
screen.update()

# Listen for left and right arrow keys
screen.listen()  # Start listening for keyboard events
screen.onkey(move_left, "Left")  # Bind the left arrow key to the move_left function
screen.onkey(move_right, "Right")  # Bind the right arrow key to the move_right function


# Keep the window open
turtle.done()
