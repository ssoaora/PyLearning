import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(2)

side = 80
angle = 90

t.fd(side)
t.right(angle)
t.fd(side)
t.right(angle)
t.fd(side)
t.right(angle)
t.fd(side + side)
t.right(angle)
t.fd(side)
t.right(angle)
t.fd(side)
t.penup()
t.goto(0,side)
t.pendown()
t.right(angle)
t.fd(side)
t.left(angle)
t.fd(side)
t.left(angle)
t.fd(side)
t.penup()
t.goto(0,-side)
t.pendown()
t.right(180)
t.fd(side)
t.right(angle)
t.fd(side)
t.penup()
t.goto(0,0)
t.right(180)
