import turtle
wn = turtle.Screen( )
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=1.0, height=1.0)
wn.tracer(0)

# border
border = turtle.Turtle()
border.goto(399, 299)
border.color("white")
border.pensize(15)
border.hideturtle()
border.fillcolor("black")
border.left(180)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle( )
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup( )
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle( )
ball.speed(-10)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle( )
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup( )
pen.hideturtle( )
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("arial", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor( )
    y += 10
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor( )
    y -= 10
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor( )
    y += 10
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor( )
    y -= 10
    paddle_b.sety(y)


# Keyboard bindings
wn.listen( )
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
running = True
while running:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor( ) > 350:
        score_a += 1
        pen.clear( )
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor( ) < -350:
        score_b += 1
        pen.clear( )
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        
    # Paddle and ball collisions
    if ball.xcor( ) < -340 and ball.ycor( ) < paddle_a.ycor( ) + 50 and ball.ycor( ) > paddle_a.ycor( ) - 50:
        ball.dx *= -1

    elif ball.xcor( ) > 340 and ball.ycor( ) < paddle_b.ycor( ) + 50 and ball.ycor( ) > paddle_b.ycor( ) - 50:
        ball.dx *= -1
    if score_a == 100 and score_b < 100:
        running = False

    elif score_b == 100 and score_a < 100:
        running = False

if score_a == 100 and score_b < 100:
    text_winner = turtle.Turtle()
    text_winner.clear()
    text_winner.color("white")
    text_winner.write("PLAYER A WON", align="center", font=("arial", 75, "underline", "bold"))
elif score_b == 100 and score_a < 100:
    text_winner = turtle.Turtle()
    text_winner.clear()
    text_winner.color("white")
    text_winner.write("PLAYER B WON", align="center", font=("arial", 75, "underline", "bold"))
