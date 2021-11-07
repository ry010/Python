import turtle
import random
t = turtle.Turtle()
c = ["purple","yellow","blue"]
t.speed(0)
t.ht()
i = int(input("Please type the number of bubbles you want to see here -> "))

for x in range(i):
    '''
    r = random.randint(0,2)
    t.color(c[r])
    '''
    t.color(c[x%3])
    r1 = random.randint(-200,200)
    r2 = random.randint(-100,100)
    t.up()
    t.goto(r1,r2)
    t.down()
    t.circle(10)
print("Thankyou for playing:)Please give us some feedback about the experience about the game.")
input("Feedback:")