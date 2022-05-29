import turtle as t
import random
import time
import os

t.bgcolor("lightgreen")
t.setup(500, 700)


class Player:
    def __init__(self, initX, initY):
        self.turtle = t.Turtle()
        self.turtle.shape("square")
        self.turtle.shapesize(1,5)
        self.turtle.up()
        self.turtle.speed(0)
        self.turtle.goto(initX,initY)
        self.score = 0

    def setColor(self, color):
        self.turtle.color(color)

    def right(self):
        if self.turtle.xcor()<200:
            self.turtle.forward(60)
    
    def left(self):
        if self.turtle.xcor()>-200:
            self.turtle.backward(60)


    def distance(self, ball) -> float : 
         return self.turtle.distance(ball)

    def getKey(self,rightKey, leftKey):
        t.onkeypress(self.right, rightKey) 
        t.onkeypress(self.left, leftKey)


class Ball:
    def __init__(self, difficulty) -> None:
        self.turtle = t.Turtle()
        self.turtle.shape("circle")
        self.turtle.shapesize(1.3)
        self.turtle.speed(0)
        self.turtle.color("white")
        self.xspeed = difficulty
        self.yspeed = difficulty
    
    def moveOn(self):
        curX, curY = self.turtle.position()
        self.turtle.goto(curX + ball_xspeed, curY + ball_yspeed)

    

playerA = Player(0, -270)
playerA.setColor("darkred")
playerB = Player(0, 270)
playerB.setColor("darkblue")


#难度选择
difficulty = t.numinput('输入难度：', '可输入1-10级', 3, 1, 10)
ball_xspeed = difficulty
ball_yspeed = difficulty

# ball = Ball(difficulty)

def promt_menu():
    txt = t.textinput('what do you want to do?','you can type [restart/quit/score]:')
    if txt=="quit":
        t.Screen().bye()
    if txt=="restart":
        t.Screen().bye()
        os.system('double.py')
    if txt=="score":
        t.goto(0,0)
        t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
        time.sleep(3)
        t.undo()


    
t.onkeypress(promt_menu,"Up")


t.listen()
playerA.getKey("Right","Left")
playerB.getKey("D", "A")
playerB.getKey("d", "a")


Ball
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")

# ball = Ball

game_on = True

# score
t.up()
t.ht()
t.goto(0,300)
t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))


while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        playerA.score = playerA.score+1
        t.clear() ##這個t是寫字的寫他們幾分的他不是ball
        time.sleep(0.5)
        ball.goto(0, -270) #這個是如果b失分了，我要讓a發球
        t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
        ball_yspeed = abs(ball_yspeed) #這是讓a發球
        ball_xspeed = abs(ball_xspeed)

        if playerA.score==3:
           ball.goto(0, 100)  
           game_on=False
           t.clear()
           t.goto(0, 50)
           t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
           t.goto(0,0)
           t.write("Game Over! player A is the winner!",False, "center",("",20))

    if ball.ycor() < -340:
        playerB.score = playerB.score+1
        t.clear()
        time.sleep(0.5)
        ball.goto(0, 270)
        t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
        ball_yspeed = -abs(ball_yspeed)
        ball_xspeed = -abs(ball_xspeed)

        if playerB.score==3:
            ball.goto(0, 100)  
            game_on=False
            t.clear()
            t.goto(0, 50)
            t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
            t.goto(0, 0)
            t.write("Game Over! playerB is the winner!", False, "center", ("", 20))


    if playerA.distance(ball) < 50 and (-260 < ball.ycor() and ball.ycor() < -245):
        ball_yspeed = abs(ball_yspeed)
        
    if playerB.distance(ball) < 50 and (245 < ball.ycor() and ball.ycor()  < 260):
        ball_yspeed = -abs(ball_yspeed)

t.done()
