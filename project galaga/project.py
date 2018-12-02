import turtle
import os
import random
wn=turtle.Screen()
wn.bgpic("space_invaders_background2.gif")
wn.bgcolor("black")
wn.title("GALAGA")
#registering shapess
turtle.addshape("player1.gif")
turtle.addshape("invader.gif")




#bordering
pen=turtle.Turtle()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.setposition(-300,-300)
pen.pendown()

pen.pensize(10)
for i in range(4):
    pen.fd (600)
    pen.lt(90)
pen.hideturtle()


#player
player=turtle.Turtle()
player.color("yellow")
player.shape("player1.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


#Player movements
playerspeed=40

#Enemy
noofenemies=6
enemies=[]
for i in range(noofenemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.speed(0)
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    x=random.randint(-250,250)
    y=random.randint(100,200)    
    enemy.setposition(x,y)

#speed of enemy
enemyspeed=5


#score
score=0
scorepen=turtle.Turtle()
scorepen.color("white")
scorepen.speed(0)
scorepen.penup()
scorepen.setposition(-280,250)
scorepen.pendown()
scorestring=("Score:%s\nCreated by :#vermajayant"%score)
scorepen.write(scorestring,False,align="Left",font=("Arial","14","normal"))
scorepen.hideturtle()

#bullet
bullet=turtle.Turtle()
bullet.color("purple")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setposition(0,0)
bullet.shapesize(0.5,0.5)
bullet.setheading(90)
bulletspeed=40
bullet.hideturtle()

bulletstate="ready"


#key assignments
def moveleft():
    x=player.xcor()
    x=x-playerspeed
    if(x<-255):
        x=-255
    player.setx(x)
def moveright():
    x=player.xcor()
    x=x+playerspeed
    if(x>255):
        x=255
    player.setx(x)
def moveup():
    y=player.ycor()
    y=y+playerspeed
    if(y>280):
        y=280
    player.sety(y)
def movedown():
    y=player.ycor()
    y=y-playerspeed
    if(y<-280):
        y=-280
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
def trace():
    player.pendown()
def nottrace():
    player.penup()
def inclineup():
    y=player.ycor()
    x=player.xcor()
    x=x+10
    y=y+20
    player.setx(x)
    player.sety(y)
turtle.listen()
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")
turtle.onkey(moveup,"Up")
turtle.onkey(movedown,"Down")
turtle.onkey(colorchange,"c")
turtle.onkey(fire,"space")
turtle.onkey(trace,"n")
turtle.onkey(nottrace,"m")
turtle.onkey(inclineup,"l")




#main loop
while (True):
    for enemy in enemies:
    
        x=enemy.xcor()
        y=enemy.ycor()
        x=x+enemyspeed
        enemy.setx(x)
        if(x>280):
            for e in enemies:
            
                y=y-10
                e.sety(y)
            enemyspeed=enemyspeed*(-1)
        if(x<-280):
            for e in enemies:
                #move all enemies down
                y=y-10
                e.sety(y)
             #change direction
            enemyspeed=enemyspeed*(-1)
        if(y<=-210):
            #limit check
            player.hideturtle()
            enemy.hideturtle()
            print("Game over")
            break
        
    
   
        
        
    
    #collision checking for bullet and enemy
        if(((bullet.xcor()-enemy.xcor())**2 + (bullet.ycor()-enemy.ycor())**2)<=500):
            enemy.hideturtle()
            x=random.randint(-250,250)
            y=random.randint(100,200)    
            enemy.setposition(x,y)
            enemy.showturtle()
            bullet.hideturtle()
            bulletstate="fire"
            score+=10
            scorestring=("Score:%s\nCreated by :#vermajayant"%score)
            scorepen.clear()
            
            scorepen.write(scorestring,False,align="Left",font=("Arial","14","normal"))
        #collision checking for player and enemy        
        if(((player.xcor()-enemy.xcor())**2 + (player.ycor()-enemy.ycor())**2)<=500):
            game=("                                                                                                                                         GAME OVER")
            scorepen.write(game,False, align="center",font=("Arial","14","normal"))
            player.hideturtle()
            print("GAME OVER")
            break

    if(((player.xcor()-enemy.xcor())**2 + (player.ycor()-enemy.ycor())**2)<=500):
        break
    
    if(enemy.ycor()<-210):
        game=("                                                                                                                                         GAME OVER")
        scorepen.write(game,False, align="center",font=("Arial","14","normal"))
                                                                                                                                                      
        break       

 
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
