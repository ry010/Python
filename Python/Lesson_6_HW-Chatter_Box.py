import turtle
t = turtle.Turtle()
c = ["green","blue","yellow","black"]
t.speed(0)

for x in range(100):
    t.color(c[x%4])
    t.fd(x)
    t.lt(91)