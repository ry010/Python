import turtle
t = turtle.Turtle()
t.speed(0)
t.ht()
c = ["red","green","blue","yellow"]
t.up()
t.goto(50,80)
t.down()

for x in range(4):
    t.color(c[x%4])
    t.begin_fill()
    t.circle(30,steps = 3)
    t.end_fill()
    '''
    for y in range(3):
        t.fd(100)
        t.left(120)
    '''
    t.lt(90)
t.color("black")
t.rt(128)
t.fd(90)
t.lt(10)
t.fd(90)
t.color("brown")
t.begin_fill()
t.rt(17)
t.circle(50,steps = 4)
t.rt(90)
t.circle(50,steps = 4)
t.rt(90)
t.circle(50,steps = 4)
t.end_fill()