import turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Mandala")

# PART 2 - CREATE THE TURTLE PEN
# turtle.Turtle() creates our drawing pen.
# speed("fastest")skips the slow animation it drs instantly.
# hideturtle() hides the arrow shape -- only the art is visible.
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

# PART 3 - OUTER COLOR SPIRAL (MOVEMENT + LOOPS + COLOR
# forward(n) moves the turtle forward n pixels
# right(91) turns into 91 degress -- 1 degree extra creates the spiral drift!
# The for loop repeats 80 times, growing the distance each round.
# colors[i % len(colors)] cycles through the color list endlessly.
colors = ["red", "orange", "yellow","lime","cyan","violet", "pink", "white"]
for i in range(80):
    board.color(colors[i % len(colors)])
    board.width(2)
    board.forward(i * 2)
    board.right(91)

# PART 4 - PEN CONTROL: MOVE TO CENTER AND DRA A FILLED STAR
# penup() lifts the pen so moving doesnt dra a line.
# goto(0,0) teleports the turtle to the exact center of the canvas
# pendown() puts the pen back on the canvas -- drawing starts again
# begin_fill() + end_fill() fills the shape with the chosen color
# A 5-pointed star turns 144 degress at each point
board.penup()
board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold","yellow")
board.begin_fill()
for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

# PART 5 - INNER PETAL RING (NESTED LOOP + FILL)
# The outer loop spins around 360 degress (36 petals x 10 degress each)
# The inner loop draws one square petal each rotation
# Nesting loops inside loops is ho complex patterns are built
board.penup()
board.goto(0,0)
board.pendown()
petal_color =["cyan","lime","violet","orange","deeppink"]
for i in range(36):
    board.color(petal_color[i % len(petal_color)],
                petal_color[(i + 2) % len(petal_color)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)

# KEEP WINDOW OPEN
turtle.done()