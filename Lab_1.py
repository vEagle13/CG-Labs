import turtle
import math

pen = turtle.Turtle()
screen = turtle.Screen()
pen.speed("fastest")
pen.hideturtle()
pen.color("white")
screen.bgcolor("black")
turtle.listen()

def f(p):
    x = (2 + 7*math.cos(math.sin(p)+math.sin(121*p)))*math.cos(p)
    y = (2 + 7*math.cos(math.sin(p)+math.sin(121*p)))*math.sin(p)
    return x,y

def event(x,y):
    pen.undo()
    pen.penup()
    pen.setpos(200,200)
    pen.color("red")
    theta = math.atan(y/x)
    if x<0:
        theta = theta + math.pi
    if y<0 and x>0:
        theta = theta + math.pi*2
    pen.write(str(f(theta)) + "\ntheta = " + str(theta))
    pass

#основна проргама
scale = 20
theta = math.pi/2800
pen.up()
while theta <= math.tau:
    x,y = f(theta)
    pen.goto(x*scale,y*scale)
    pen.down()
    theta = theta + 0.005
screen.onscreenclick(event,3)
turtle.mainloop()
