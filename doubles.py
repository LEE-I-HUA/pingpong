import turtle as t
import random
import time
import os

t.bgcolor("lightpink")
t.setup(500, 700)

def rightA():
    if playerA.xcor()<200:
        playerA.forward(60)
        
def rightB():
    if playerB.xcor()<200:
        playerB.forward(60)        

def leftA():
    if playerA.xcor()>-200:
        playerA.backward(60)

def leftB():
    if playerB.xcor()>-200:
        playerB.backward(60)

#难度选择
difficulty = t.numinput('输入难度：', '可输入1-10级', 3, 1, 10)
ball_xspeed = difficulty
ball_yspeed = difficulty

def promt_menu():
    txt = t.textinput('what do you want to do?','you can type [restart/quit/score]:')
    if txt=="quit":
        t.Screen().bye()
    if txt=="restart":
        t.Screen().bye()
        os.system('double.py')
    if txt=="score":
        t.goto(0,0)
        t.write(f"Ascore : {Ascore},Bscore : {Bscore}", False, "center", ("", 15))
        time.sleep(3)
        t.undo()
    t.listen()
    t.onkeypress(rightA,"Right")
    t.onkeypress(leftA,"Left")
    t.onkeypress(rightB,"D")
    t.onkeypress(rightB,"d")
    t.onkeypress(leftB,"A")
    t.onkeypress(leftB,"a")
    
t.onkeypress(promt_menu,"Up")


#playerA
playerA = t.Turtle()
playerA.shape("square")
playerA.shapesize(1,5)
playerA.up()
playerA.speed(0)
playerA.goto(0,-270)

#playerB
playerB = t.Turtle()
playerB.shape("square")
playerB.shapesize(1,5)
playerB.up()
playerB.speed(0)
playerB.goto(0,270)

#Ball
ball = t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")

t.listen()
t.onkeypress(rightA,"Right")
t.onkeypress(leftA,"Left")
t.onkeypress(rightB,"D")
t.onkeypress(rightB,"d")
t.onkeypress(leftB,"A")
t.onkeypress(leftB,"a")

game_on = True
Bscore=0
Ascore=0

#life score
t.up()
t.ht()
t.goto(0,300)
t.write(f"Ascore : {Ascore},Bscore : {Bscore}", False, "center", ("", 15))


while game_on:
    new_x = ball.xcor() + ball_xspeed
    new_y = ball.ycor() + ball_yspeed
    ball.goto(new_x, new_y)

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball_xspeed *= -1

    if ball.ycor() > 340:
        Bscore = Bscore+1
        t.clear()
        time.sleep(0.5)
        ball.goto(0, 100) 
        t.write(f"Ascore : {Ascore}, Bscore : {Bscore}", False, "center", ("", 15))
        ball_yspeed *= -1
        ball_xspeed *= -1

        if Bscore==3:
           game_on=False
           t.clear()
           t.goto(0, 50)
           t.write(f"Ascore : {Ascore},Bscore : {Bscore}", False, "center", ("", 15)) 
           t.goto(0,0)
           t.write("Game Over!B is the winner!",False, "center",("",20))

    if ball.ycor() < -340:
        Ascore = Ascore+1
        t.clear()
        time.sleep(0.5)
        ball.goto(0, 100)
        t.write(f"Ascore : {Ascore},Bscore : {Bscore}", False, "center", ("", 15))
        ball_yspeed *= -1
        ball_xspeed *= -1

        if Ascore==3:
            game_on=False
            t.clear()
            t.goto(0, 50)
            t.write(f"Ascore : {Ascore},Bscore : {Bscore}", False, "center", ("", 15)) 
            t.goto(0, 0)
            t.write("Game Over!A is the winner!", False, "center", ("", 20))


    if playerA.distance(ball) < 50 and -260 < ball.ycor() < -245:
        ball_yspeed *= -1
        
    if playerB.distance(ball) < 50 and 245 < ball.ycor() < 260:
        ball_yspeed *= -1


t.done()

