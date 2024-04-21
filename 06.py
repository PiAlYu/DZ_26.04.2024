from turtle import *

tracer(20)
n = 20
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * n, y * n)
        dot(3)
home()
down()
left(90)
for i in range(4):
    for y in range(3):
        forward(2 * n)
        left(270)
    forward(5 * n)
up()
done()