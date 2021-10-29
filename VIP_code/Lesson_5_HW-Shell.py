import turtle
t = turtle.Turtle()
t.speed(0)
t.shape("turtle")
t.color("blue","red")
t.pensize(1)

for x in range(100):
    t.circle(x)
    t.left(10)
    
a = "SH"
b = "ELL"
print(a+b)

t.ht()