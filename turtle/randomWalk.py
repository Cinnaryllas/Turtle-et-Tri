import turtle
import random

turtle.colormode(255)
turtle.delay(0)
maTortue0 = turtle.Turtle()
maTortue0.speed(0)
maTortue1 = maTortue0.clone()
maTortue2 = maTortue0.clone()
maTortue3 = maTortue0.clone()
maTortue4 = maTortue0.clone()

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

randomColor(maTortue0)
randomColor(maTortue1)
randomColor(maTortue2)
randomColor(maTortue3)
randomColor(maTortue4)

while 1 != 2:
    infinitoDriftuuu(maTortue0)
    infinitoDriftuuu(maTortue1)
    infinitoDriftuuu(maTortue2)
    infinitoDriftuuu(maTortue3)
    infinitoDriftuuu(maTortue4)