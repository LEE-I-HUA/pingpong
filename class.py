#! /usr/bin/python3
import turtle as t
import time
import os

class Player:
	def __init__(self, initX, initY) -> None:
		self.turtle = t.Turtle()
		self.turtle.shape("square")
		self.turtle.shapesize(1,5)
		self.turtle.up()
		self.turtle.speed(0)
		self.turtle.goto(initX,initY)
		self.score = 0

	def setColor(self, color) -> None:
		self.turtle.color(color)

	def right(self) -> None:
		if self.turtle.xcor()<200 : self.turtle.forward(60) 
			
	def left(self) -> None:
		if self.turtle.xcor()>-200 : self.turtle.backward(60)
			
	def distance(self, ball) -> float : 
		return self.turtle.distance(ball)

	def bindKey(self,rightKey, leftKey) -> None:
		t.onkeypress(self.right, rightKey) 
		t.onkeypress(self.left, leftKey)

	def position(self) -> tuple:
		return self.turtle.position()

class Ball:
	def __init__(self, difficulty) -> None:
		self.turtle = t.Turtle()
		self.turtle.shape("circle")
		self.turtle.shapesize(1.3)
		self.turtle.speed(0)
		self.turtle.color("white")
		self.xspeed = difficulty
		self.yspeed = difficulty
		self.turtle.up()
	
	def moveOn(self) -> None:
		curX, curY = self.turtle.position()
		self.turtle.goto(curX + self.xspeed, curY + self.yspeed)

	def xRebound(self) -> None:
		self.xspeed = -abs(self.xspeed)*self.xcor()/abs(self.xcor())

	def xcor(self) -> int:
		return self.turtle.xcor()
	
	def ycor(self) -> int:
		return self.turtle.ycor()

	def getPosition(self) -> tuple:
		return self.turtle.position()

	def getXSpeed(self) -> int:
		return self.xspeed

	def getYSpeed(self) -> int:
		return self.yspeed

	def setXSpeed(self, xspeed) -> None:
		self.xspeed = xspeed

	def setYSpeed(self, yspeed) -> None:
		self.yspeed = yspeed

	def goto(self, x, y=None):
		self.turtle.goto(x) if y is None else self.turtle.goto(x,y)

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

def finishThisRound( playerA, playerB, ball):
	winner, loser = (playerA, playerB) if playerA.distance(ball.getPosition()) > playerB.distance(ball.getPosition()) else (playerB, playerA)
	winner.score += 1
	winX, winY = winner.position()
	printScore(playerA.score, playerB.score)
	time.sleep(0.5)
	pingpong.goto(winX, winY)
	pingpong.setYSpeed(-winY/abs(winY)* abs(pingpong.getYSpeed())) 

def printScore(p1Score, p2Score):
	t.clear()
	t.goto(0, 300)
	t.write(f"Ascore : {p1Score},Bscore : {p2Score}", False, "center", ("", 15))

def endGame(playerA, playerB):
	pingpong.goto(0, 100)  
	t.clear()
	t.goto(0, 50)
	t.write(f"Ascore : {playerA.score},Bscore : {playerB.score}", False, "center", ("", 15))
	t.goto(0,0)
	t.write("Game Over! player {} is the winner!".format("A" if playerA.score > playerB.score else "B"), False, "center",("",20))

difficulty = t.numinput('输入难度：', '可输入1-10级', 3, 1, 10)
pingpong = Ball(difficulty)
playerA = Player(0, -270)
playerB = Player(0, 270)
playerA.setColor("darkred")
playerB.setColor("darkblue")
playerA.bindKey("Right","Left")
playerB.bindKey("D", "A")
playerB.bindKey("d", "a")
t.bgcolor("lightgreen")
t.setup(500, 700)
t.onkeypress(promt_menu,"Up")
t.listen()
t.up()
t.ht()
printScore(playerA.score, playerB.score)
game_on = True

while game_on:
	pingpong.moveOn()
	if pingpong.xcor() > 240 or pingpong.xcor() < -240: pingpong.xRebound()
	if pingpong.ycor() > 340 or pingpong.ycor() < -340:	finishThisRound(playerA, playerB, pingpong)			
	if playerA.score == 3 or playerB.score == 3: 
		endGame(playerA, playerB)
		game_on = False
	if playerA.distance(pingpong.getPosition()) < 50 and (-260 < pingpong.ycor() and pingpong.ycor() < -245): pingpong.setYSpeed(abs(pingpong.getYSpeed()))      
	if playerB.distance(pingpong.getPosition()) < 50 and (245 < pingpong.ycor() and pingpong.ycor() < 260): pingpong.setYSpeed(-abs(pingpong.getYSpeed()))
t.done()
