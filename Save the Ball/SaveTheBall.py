################################################
# NAME = SAVE THE BALL                         #
# Developed by = Utkarsh Mishra                #
# Source Code = Python                         #
# Date=09-01-2018                              #
################################################

import turtle
import os
import random


#Set screen
screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Save The Ball")
screen.bgpic("Snow.gif")

#Set the border
border_pen=turtle.Turtle()
border_pen.color("white")
border_pen.penup()
border_pen.speed(0)
border_pen.setposition(-600,-300)
border_pen.pensize(10)
border_pen.pendown()
border_pen.fd(1200)
border_pen.lt(90)
border_pen.fd(600)
border_pen.lt(90)
border_pen.fd(1200)
border_pen.lt(90)
border_pen.fd(600)
border_pen.lt(90)
#creating boundarylines
border_pen.penup()
border_pen.setposition(-585,250)
border_pen.color("red")
border_pen.pendown()
border_pen.fd(1170)
border_pen.penup()
border_pen.setposition(-585,-250)
border_pen.color("red")
border_pen.pendown()
border_pen.fd(1170)
border_pen.hideturtle()

#create the bars
#create BAR1
bar1=turtle.Turtle()
bar1.color("purple")
bar1.shape("square")
bar1.shapesize(0.75,8)
bar1.penup()
bar1.setposition(0,230)
#create BAR2
bar2=turtle.Turtle()
bar2.color("purple")
bar2.shape("square")
bar2.shapesize(0.75,8)
bar2.penup()
bar2.setposition(0,-230)

barspeed=20

#Commands
def move_rightbar1():
    x=bar1.xcor()
    x+=barspeed
    if(x>500):
        x=500
    bar1.setx(x)

def move_leftbar1():
    x=bar1.xcor()
    x-=barspeed
    if(x<-500):
        x=-500
    bar1.setx(x)

def move_rightbar2():
    x=bar2.xcor()
    x+=barspeed
    if(x>500):
        x=500
    bar2.setx(x)

def move_leftbar2():
    x=bar2.xcor()
    x-=barspeed
    if(x<-500):
        x=-500
    bar2.setx(x)

#link to keyboard
turtle.listen()
turtle.onkey(move_leftbar1,"a")
turtle.onkey(move_rightbar1,"d")
turtle.onkey(move_leftbar2,"Left")
turtle.onkey(move_rightbar2,"Right")    

#create the ball
ball=turtle.Turtle()
ball.color("green")
ball.shape("circle")
ball.penup()
ball.speed(0)
ball.setposition(random.randint(-70,70),-210)
ballspeed=2

score=0
score_pen=turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()
#MAIN LOOP
while True:    
    #displaying score
    
    score_pen.color("white")
    score_pen.setposition(0,320)
    scorestring="SCORE=%s"%score
    score_pen.pendown()
    score_pen.clear()
    score_pen.write(scorestring,False,align="center",font=("Arial",20,"normal"))
    score_pen.penup()
    
    #check ball collision with bar2
    if(ball.ycor()<=-207 and ball.xcor()<=(bar2.xcor()+75) and ball.xcor()>=(bar2.xcor()-75)):
        score+=10
        x=ball.xcor()        
        x2=bar2.xcor()       
        ball.setheading(90-(x-x2))
        while(ball.ycor()<=207):
            #y=ball.ycor()
            #ball.sety(y+2)
            ball.fd(ballspeed)
            if(ball.xcor()<=-580 or ball.xcor()>=580):
                ball.setheading(180-ball.heading())
    #check ball collision with bar1
    elif(ball.ycor()>=207 and ball.xcor()<=(bar1.xcor()+75) and ball.xcor()>=(bar1.xcor()-75)):
        score+=10
        x=ball.xcor()        
        x2=bar1.xcor()       
        ball.setheading((x-x2)-90)
        while(ball.ycor()>=-207):
            #y=ball.ycor()
            #ball.sety(y-2)
            ball.fd(ballspeed)
            if(ball.xcor()<=-580 or ball.xcor()>=580):
                ball.setheading(180-ball.heading())                
    else:
        score_pen.setposition(0,0)
        score_pen.pendown()
        scorestring="SCORE=%s\nGAME OVER"%score
        score_pen.clear()
        score_pen.write(scorestring,False,align="center",font=("Arial",40,"normal"))
        score_pen.hideturtle()
        score_pen.penup()
        break
    ballspeed+=0.10
print(ball.position(),ball.heading())
input()













    
