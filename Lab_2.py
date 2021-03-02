import turtle

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def ice(x1,y1,x2,y2,i):
    start = x1,y1
    end = x2,y2
    pen.up()
    pen.goto(start)
    dist = pen.distance(end)
    pen.seth(pen.towards(end))
    pen.down()
    p1 = (x1+x2)/2,(y1+y2)/2
    pen.goto(p1)
    pen.right(90)
    pen.fd(dist*0.33)
    p2 = pen.xcor(),pen.ycor()
    pen.bk(dist*0.33)
    pen.left(90)
    pen.goto(end)
    if (i>0):
        ice(start[0],start[1],p1[0],p1[1],i-1),
        ice(p1[0],p1[1],p2[0],p2[1],i-1),
        ice(p2[0],p2[1],p1[0],p1[1],i-1),
        ice(p1[0],p1[1],end[0],end[1],i-1)
    pass

sc = 150
ice(-sc,sc,sc,sc,3)
ice(sc,sc,sc,-sc,3)
ice(sc,-sc,-sc,-sc,3)
ice(-sc,-sc,-sc,sc,3)

turtle.mainloop()



