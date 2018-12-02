
import turtle
import os
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("GALGA")
#bordering
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for i in range(4):
    pen.fd(600)
    pen.lt(90)
pen.hideturtle()
#player
player=turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
#Player movements
playerspeed=20


#bullet
bullet=turtle.Turtle()
bullet.color("purple")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setposition(0,0)
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bulletspeed=20


bulletstate="ready"


#key assignments
def moveleft():
    x=player.xcor()
    x=x-playerspeed
    if(x<-290):
        x=-290
    player.setx(x)
def moveright():
    x=player.xcor()
    x=x+playerspeed
    if(x>290):
        x=290
    player.setx(x)
def moveup():
    y=player.ycor()
    y=y+playerspeed
    if(y>290):
        y=290
    player.sety(y)
def movedown():
    y=player.ycor()
    y=y-playerspeed
    if(y<-290):
        y=-290
    player.sety(y)
def colorchange():
    player.color("red")
def fire():
    global bulletstate
    if(bulletstate=="ready"):
         bulletstate="fire"
         x=player.xcor()
         y=player.ycor()+10
         bullet.setposition(x,y)
         bullet.showturtle()
         

turtle.listen()
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
turtle.onkey(moveup,"Up")
turtle.onkey(movedown,"Down")
turtle.onkey(colorchange,"c")
turtle.onkey(fire,"space")
#player2
player2=turtle.Turtle()
player2.color("yellow")
player2.shape("triangle")
player2.penup()
player2.speed(0)
player2.setposition(-50,-250)
player2.setheading(90)
#Player movements
playerspeed2=20

#Enemy
enemy=turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(0,200)
enemyspeed=2






def moveleft():
    x=player2.xcor()
    x=x-playerspeed2
    if(x<-290):
        x=-290
    player2.setx(x)
def moveright():
    x=player2.xcor()
    x=x+playerspeed2
    if(x>290):
        x=290
    player2.setx(x)
def moveup():
    y=player2.ycor()
    y=y+playerspeed2
    if(y>290):
        y=290
    player2.sety(y)
def movedown():
    y=player2.ycor()
    y=y-playerspeed2
    if(y<-290):
        y=-290
    player2.sety(y)
def colorchange():
    player2.color("purple")

turtle.listen()
turtle.onkey(moveleft,"a")
turtle.onkey(moveright,"d")
turtle.onkey(moveup,"w")
turtle.onkey(movedown,"s")
turtle.onkey(colorchange,"b")

#main loop
while (True):
    
    x=enemy.xcor()
    y=enemy.ycor()
    x=x+enemyspeed
    enemy.setx(x)
    if(x>=290):
        enemyspeed=enemyspeed*(-1)
        y=y-20
        enemy.sety(y)
    if(x<=-290):
        enemyspeed=enemyspeed*(-1)
        y=y-20
        enemy.sety(y)
 
#bullet moving
    if(bulletstate=="fire"):
        
        y1=bullet.ycor()
        y1=y1+bulletspeed
        bullet.sety(y1)
        #ensuring bullet stays in box
    if(bullet.ycor()>280):
                
        bulletstate="ready"
        bullet.hideturtle()
            









hold=input("enter the input")
