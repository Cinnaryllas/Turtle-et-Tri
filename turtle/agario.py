import turtle
import random

turtle.Screen().screensize(100,100)
turtle.colormode(255)
turtle.delay(0)

tortueUser = turtle.Turtle()
tortueUser.speed(1)
tortueUser.shape("circle")
tortueUser.shapesize(1,1,1)
tortueUser.penup()

tortues=[]

for i in range(10):
    tortues.append(turtle.Turtle())
    tortues[i].speed(10)
    tortues[i].shape("circle")
    tortues[i].shapesize(1,1,1)

def infinitoDriftuuu(Tortue):
    Tortue.forward(3)
    alea = random.randint(0,2)
    if (alea == 0):
        Tortue.left(90)
    elif (alea == 1):
        Tortue.right(90)
    else:
        Tortue.forward(3)

def randomColor(Tortue):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    Tortue.color(r,g,b)

for i in tortues:
    randomColor(i)

def randomStartPos(Tortue):
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    Tortue.penup()
    Tortue.goto(x,y)

for i in tortues:
    randomStartPos(i)

def miamTortue(Tortue1, Tortue2):
    eat = random.randint(0,1)
    distance = (Tortue1.xcor()-Tortue2.xcor())**2 + (Tortue1.ycor()-Tortue2.ycor())**2
    distance**(0.5)
    if(distance < (Tortue1.shapesize()[0]+Tortue2.shapesize()[0])*100):
        if Tortue1.shapesize() > Tortue2.shapesize():
            Tortue1.shapesize(Tortue1.shapesize()[0]+Tortue2.shapesize()[0],Tortue1.shapesize()[0]+Tortue2.shapesize()[0],Tortue1.shapesize()[0]+Tortue2.shapesize()[0])
            Tortue2.hideturtle()
            Tortue1.speed()
            return (tortues.remove(Tortue2))
        elif Tortue2.shapesize() > Tortue1.shapesize():
            Tortue2.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[0]+Tortue1.shapesize()[0])
            Tortue1.hideturtle()
            Tortue2.speed()
            return (tortues.remove(Tortue1))
        elif Tortue1.shapesize() == Tortue2.shapesize():
            if eat==0:
                Tortue1.shapesize(Tortue1.shapesize()[0]+Tortue2.shapesize()[0],Tortue1.shapesize()[0]+Tortue2.shapesize()[0],Tortue1.shapesize()[0]+Tortue2.shapesize()[0])
                Tortue2.hideturtle()
                Tortue1.speed()
                return (tortues.remove(Tortue2))
            elif eat==1:
                Tortue2.shapesize(Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[0]+Tortue1.shapesize()[0],Tortue2.shapesize()[0]+Tortue1.shapesize()[0])
                Tortue1.hideturtle()
                Tortue2.speed()
                return (tortues.remove(Tortue1))

def playerRight():
    tortueUser.right(90)

def playerLeft():
    tortueUser.left(90)

turtle.listen()
turtle.onkeypress(playerRight,"d")
turtle.onkeypress(playerLeft,"q")

while 1 != 2:
    tortueUser.forward(3)

    for i in tortues:
        infinitoDriftuuu(i)

    for i in tortues:
        miamTortue(tortueUser,i)
        for y in tortues:
            if i !=y:
                miamTortue(i,y)