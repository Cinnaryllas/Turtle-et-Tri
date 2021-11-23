import turtle

maTortue = turtle.Turtle()
turtle.delay(0)

def flocon(n, cote):
    if n == 0:
        maTortue.forward(cote)
    else :
        flocon(n-1, cote/3)
        maTortue.left(60)
        flocon(n-1, cote/3)
        maTortue.left(-120)
        flocon(n-1, cote/3)
        maTortue.left(60)
        flocon(n-1, cote/3)

maTortue.setheading(0)
maTortue.hideturtle()
maTortue.speed(0)
maTortue.up()
maTortue.goto(-280,100)
maTortue.down()

i=0
while i!=4:
    flocon(n = 10, cote = 2500)
    maTortue.left(-120)
    i+1
input()