import turtle as t
import random
import time

class Player:
    def __init__(self, initX, initY):
        self.turtle = t.Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(1,5)
        self.turtle.up()
        self.turtle.speed(0)
        self.turtle.goto(initX,initY)
        self.score = 0

    def right(self):
        if self.turtle.xcor()<200:
            self.turtle.forward(50)
    
    def left(self):
        if self.turtle.xcor()>-200:
            self.turtle.backword(50)

    def distance(self, ball) -> float : 
        return self.turtle.distance(ball)

    def end(lowerBound, upperBound):
        if Player.distance(ball) < 50 and lowerBound< ball.ycor() < upperBound:
            ball_yspeed *= -1


class Ball:
    def __init__(self) -> None:
        self.turtle = t.Turtle()
        self.turtle.shape("circle")
        self.turtle.shapesize(1.3)
        self.turtle.speed(0)
        self.turtle.color("white")
        self.xspeed = 5
        self.yspeed = 5
    
    def moveOn(self):
        curX, curY = self.turtle.position()
        self.turtle.goto(curX + ball_xspeed, curY + ball_yspeed)

    def slowDown(self):
        



    #def xcor
# new_x = ball.xcor() + ball_xspeed
# new_y = ball.ycor() + ball_yspeed
# ball.goto(new_x, new_y)
        
# ball_xspeed = 5
# ball_yspeed = 5
# initialize
t.bgcolor("lightpink")
t.setup(500, 700)
pA = Player(0, 270)
pB = Player(0, -270)
b = Ball()

#Ball
#  ball = t.Turtle()
# ball.shape("circle")
# ball.shapesize(1.3)
# ball.up()
# ball.speed(0)ball
# ball.color("white")

t.listen()
t.onkeypress(pA.right,"Right")
t.onkeypress(pA.left,"Left")
t.onkeypress(pB.right,"D")
t.onkeypress(pB.right,"d")
t.onkeypress(pB.left,"A")
t.onkeypress(pB.left,"a")



game_on = True


#life score
t.up()
t.ht()
t.goto(0,300)
t.write(f"Ascore : {pA.score},Bscore : {pB.score}", False, "center", ("", 15))


while game_on:
    b.moveOn()

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        pB.score += 1
        t.clear()
        time.sleep(0.5)
        ball.goto(0, 100)
        t.write(f"Ascore : {pA.score}, Bscore : {pB.score}", False, "center", ("", 15))
        ball_yspeed *= -1
        ball_xspeed *= -1

    if ball.ycor() < -340:
        pA.score += 1
        t.clear()
        time.sleep(0.5)
        ball.goto(0, 100)
        t.write(f"Ascore : {pA.score},Bscore : {pB.score}", False, "center", ("", 15))
        ball_yspeed *= -1
        ball_xspeed *= -1

    if pA.score==3 or pB.score==3:
        game_on=False
        t.goto(0, 0)
        t.write("Game Over", False, "center", ("", 20))

    pA.end(-260, -245)

    pB.end(245, 260)


    # if pA.distance(ball) < 50 and -260 < ball.ycor() < -245:
    #     ball_yspeed *= -1
        
    # if pB.distance(ball) < 50 and 245 < ball.ycor() < 260:
    #     ball_yspeed *= -1


t.done()
