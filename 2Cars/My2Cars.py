#======================================#
# 2 Cars                               #
# Date=16-01-2018 Time=19:51           #
# Utkarsh Mishra                       #
#======================================#


#importing modules required
import turtle
import os
import random

turtle.register_shape("car1.gif")
turtle.register_shape("car2.gif")
turtle.register_shape("coin.gif")
turtle.register_shape("police2.gif")
#turtle.register_shape("police1.gif")

#create window
win=turtle.Screen()
win.title("2 Cars")
win.bgcolor("white")

#create boundaries
bpen=turtle.Turtle()
bpen.penup()
bpen.speed(0)
bpen.pencolor("blue")
bpen.pensize("4")
bpen.setposition(450,340)
bpen.rt(90)
bpen.pendown()
bpen.fd(680)
bpen.penup()
bpen.setposition(-450,340)
bpen.pendown()
bpen.fd(680)
bpen.hideturtle()


#create cars
#create CAR1
car1=turtle.Turtle()
car1.hideturtle()
car1.shape("car1.gif")
car1.color("black")
car1.shapesize(3)
car1.speed(0)
car1.penup()
car1.setposition(-330,-300)
car1.setheading(90)
car1.showturtle()
car1pos="LEFT"

#create CAR2
car2=turtle.Turtle()
car2.hideturtle()
car2.shape("car2.gif")
car2.color("white")
car2.shapesize(3)
car2.speed(0)
car2.penup()
car2.setposition(330,-300)
car2.setheading(90)
car2.showturtle()
car2pos="RIGHT"



#create barrier
no_barriers=3
#barrier1
pos1=[-330,-110]
barriers1=[]
poslisty1=[] #position list(containing y-cor) of barriers1 and bonus1
for i in range (no_barriers):
    barriers1.append(turtle.Turtle())
y=350
for barrier1 in barriers1:
    i=barriers1.index(barrier1)
    barrier1.hideturtle()
    barrier1.penup()
    barrier1.speed(0)
    barrier1.shape("police2.gif")
    barrier1.setposition(pos1[random.randint(0,1)],random.randint(y+100,y+300))
    x,y=barrier1.position()
    poslisty1.append(y)
    #barrier1.color("red")
    barrier1.showturtle()
print(poslisty1)

#barriers1[1].shape("police2.gif")
#barrier2
pos2=[330,110]
barriers2=[]
poslisty2=[]#position list(containing y-cor) of barriers2
for i in range (no_barriers):
    barriers2.append(turtle.Turtle())
y=350
for barrier2 in barriers2:
    i=barriers2.index(barrier2)
    barrier2.speed(0)
    barrier2.hideturtle()
    barrier2.penup()
    barrier2.shape("police2.gif")
    barrier2.setposition(pos2[random.randint(0,1)],random.randint(y+100,y+300))
    x,y=barrier2.position()
    poslisty2.append(y)
    #barrier2.color("red")
    barrier2.showturtle()
print(poslisty2)
#barriers2[1].shape("police1.gif")
#speed of barrier approach
barrierspeed=30


#create BONUS
no_bonus=3
#bonus1
bonus_1=[]
for i in range(no_bonus):
    bonus_1.append(turtle.Turtle())
for bonus1 in bonus_1:
    y=poslisty1[-1]
    bonus1.hideturtle()
    bonus1.penup()
    bonus1.speed(0)
    bonus1.shape("coin.gif")
    bonus1.setposition(pos1[random.randint(0,1)],random.randint(y+100,y+300))
    x,y=bonus1.position()
    poslisty1.append(y)
    #bonus1.color("yellow")
    bonus1.showturtle()
print(poslisty1)

#bonus2
bonus_2=[]
for i in range(no_bonus):
    bonus_2.append(turtle.Turtle())
for bonus2 in bonus_2:
    y=poslisty2[-1]
    bonus2.hideturtle()
    bonus2.penup()
    bonus2.speed(0)
    bonus2.shape("coin.gif")
    bonus2.setposition(pos2[random.randint(0,1)],random.randint(y+100,y+300))
    x,y=bonus2.position()
    poslisty2.append(y)
    #bonus2.color("yellow")
    bonus2.showturtle()
print(poslisty2)





#binding functions

def move_left1():
    global car1pos
    if car1pos != "LEFT":
        car1.setposition(-330,-300)
        car1pos="LEFT"

def move_right1():
    global car1pos
    if car1pos != "RIGHT":
        car1.setposition(-110,-300)
        car1pos="RIGHT"

def move_left2():
    global car2pos
    if car2pos != "LEFT":
        car2.setposition(110,-300)
        car2pos="LEFT"


def move_right2():
    global car2pos
    if car2pos != "RIGHT":
        car2.setposition(330,-300)
        car2pos="RIGHT"


#keyboard binding
turtle.listen()
turtle.onkey(move_left1,"a")
turtle.onkey(move_right1,"d")
turtle.onkey(move_left2,"Left")
turtle.onkey(move_right2,"Right")


#vary the position of bar
def vary_bar(bar,n=1):
    global poslisty1,poslisty2
    x=bar.xcor()
    y=bar.ycor()
    y-=barrierspeed
    if(y<=-280):
        bar.hideturtle()
        if(bar.xcor()<0):
            x=pos1[random.randint(0,1)]
            y=int(abs(max(poslisty1)))
            y=random.randint(y+100,y+200)
            poslisty1[n]=y
        else:
            x=pos2[random.randint(0,1)]
            y=int(abs(max(poslisty2)))
            y=random.randint(y+100,y+200)
            poslisty2[n]=y

    bar.setposition(x,y)
    bar.showturtle()


#check for collision of bar with car
def isCollision(bar,car):
    if bar.xcor()==car.xcor() and bar.ycor()<=-280:
        bar.hideturtle()
        return True
    return False

running=True
score=0
while running:
    for i in range(no_barriers):
        vary_bar(barriers1[i],i)
        vary_bar(barriers2[i],i)
        vary_bar(bonus_1[i],i+no_barriers)
        vary_bar(bonus_2[i],i+no_barriers)
        print("poslisty1=",poslisty1,"     poslisty2=",poslisty2)
        if isCollision(bonus_1[i],car1):
            score+=10
        if isCollision(bonus_2[i],car2):
            score+=10
        if isCollision(barriers1[i],car1):
            running=False
            break
        if isCollision(barriers2[i],car2):
            running=False
            break
    
    barrierspeed+=0.01
print (score)
    





















    
    







































