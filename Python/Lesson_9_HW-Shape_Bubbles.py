import turtle
import random
t = turtle.Turtle()
c = ["blue","red","yellow","purple","green"]
t.speed(0)
i = int(input("Type how many shapes you want to stamp."))
t.ht()

for x in range(i):
    t.color(c[x%5])
    r1 = random.randint(-200,200)
    r2 = random.randint(-200,200)
    t.up()
    t.goto(r1,r2)
    t.down()
    t.begin_fill()
    r = random.randint(1,3)
    if r==1:
        t.circle(-10, steps = 3)
    elif r==2:
        t.circle(10)
    else:
        t.circle(10,steps = 6)
    t.end_fill()