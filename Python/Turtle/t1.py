import math
import turtle

bob = turtle.Turtle()

for s in str(math.pi)[2:]:
    bob.forward(int(s)*10)
    bob.left(int(s)*10)

turtle.done()