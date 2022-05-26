import turtle as t
import random
import time

t.bgcolor("lightpink")
t.setup(500, 700)

class player():
    def __init__(self):
        self.player = t.Turtle()
        self.player.shape("square")
        self.player.shapesize(1,5)
        self.player.up()
        self.player.speed(0)
        self.player.goto(0,-270)
        
class playerOnCourt(player) :
    
    def setPosition(self, yAxis):                 
        player.goto(0,yAxis)

    def right(self):
        if player.xcor()<200:
            player.forward(10)

    def left(self):
        if player.xcor()>-200:
            player.backward(10)



playerA = playerOnCourt.setPosition(-270)
playerB = playerOnCourt.setPosition(150)



#Ball
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")

t.listen()
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")

ball_xspeed = 5
ball_yspeed = 5

game_on = True
life = 3

#life score
t.up()
t.ht()
t.goto(0,300)
t.write(f"life : {life}", False, "center", ("", 20))

while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        ball_yspeed *= -1

    if ball.ycor() < -340:
        life -= 1
        t.clear()
        t.write(f"life : {life}", False, "center", ("", 20))
        time.sleep(0.5)
        ball.goto(0, 100)
        ball_yspeed *= -1
        ball_xspeed *= -1

        if life==0:
            game_on = False
            t.goto(0,0)
            t.write("Game Over", False, "center", ("", 20))

    if player.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1
