import turtle

turtle.delay(0)
maTortue = turtle.Turtle()
maTortue.speed(0)

for i in range (50000):
    maTortue.forward(1)
    maTortue.left(1*(1000/(i+1)))

input()