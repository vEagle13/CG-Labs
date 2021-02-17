import turtle
import math

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed("fastest")
pen.hideturtle()
pen.color("white")
screen.bgcolor("black")

def f(p):
    x = (2 + 7*math.cos(math.sin(p)+math.sin(121*p)))*math.cos(p)
    y = (2 + 7*math.cos(math.sin(p)+math.sin(121*p)))*math.sin(p)
    return x,y

#основна проргама
scale = 20
theta = math.pi/2800
pen.up()
while theta <= math.tau:
    x,y = f(theta)
    pen.goto(x*scale,y*scale)
    pen.down()
    theta = theta + 0.001

turtle.mainloop()
