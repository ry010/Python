import turtle
t = turtle.Turtle()

t.color("red")
t.circle(80)
t.color("blue")
t.circle(60)
t.color("yellow")
t.circle(40)
t.color("pink")
t.circle(20)

t.color("red")

t.forward(80)
t.right(150)
t.forward(50)
t.right(60)
t.forward(50)
t.left(30)

t.forward(80)
t.left(150)
t.forward(50)
t.left(60)
t.forward(50)
t.right(120)

t.color("black")

t.forward(160)
t.left(90)
t.begin_fill()
t.circle(-10)
t.end_fill()

t.hideturtle()