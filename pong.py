import turtle

#### Variables ####

score_a = 0
score_b = 0
first_player = ''
second_player = ''

#### Game screen ####

wn = turtle.Screen()
start_first = turtle.textinput('Name First Player', '{}'.format(first_player))
start_second = turtle.textinput('Name Second Player', '{}'.format(second_player))
wn.title('Pong By Davide Cannerozzi')
wn.setup(800, 600)
wn.bgcolor('black')
wn.tracer(0)

#### Paddle Left ####

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(stretch_wid=4, stretch_len=1)
paddle_left.color('blue')
paddle_left.penup()
paddle_left.goto(-300, 0)

#### Paddle Right ####

paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('red')
paddle_right.shapesize(stretch_wid=4, stretch_len=1)
paddle_right.penup()
paddle_right.goto(300, 0)

#### Ball ####

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

#### Paddle Move ####

def paddle_left_up():
    current_y = paddle_left.ycor()
    current_y += 20
    paddle_left.sety(current_y)

def paddle_left_down():
    current_y = paddle_left.ycor()
    current_y -= 20
    paddle_left.sety(current_y)

def paddle_right_up():
    current_y = paddle_right.ycor()
    current_y += 20
    paddle_right.sety(current_y)

def paddle_right_down():
    current_y = paddle_right.ycor()
    current_y -= 20
    paddle_right.sety(current_y)

#### Keyboard Binding ####

wn.listen()
wn.onkeypress(paddle_left_up, 'q')
wn.onkeypress(paddle_left_down, 'a')
wn.onkeypress(paddle_right_up, 'o')
wn.onkeypress(paddle_right_down, 'l')


while True:
    wn.update()

    #### Ball movement ####
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #### Score ####
    score = turtle.Turtle()
    score.color('white')
    score.penup()
    score.speed(0)
    score.goto(0, 250)
    score.shape('blank')
    score.write('{} : {} , {} : {} '.format(start_first, score_a, start_second, score_b),
                align='center',
                font=("Arial", 22, "normal"))

    #### BOUNCING BALL: TOP AND BOTTOM BORDERS ####
    if ball.ycor() > 290:
       ball.sety(290)
       ball.dy *= -1

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1

    #### BOUNCING BALL: LEFT AND RIGHT BORDERS ####
    if ball.xcor() > 390:
       ball.goto(0, 0)
       score_a+= 1

    if ball.xcor() < -390:
       ball.goto(0, 0)
       score_b+= 1





