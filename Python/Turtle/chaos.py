import random
import turtle


def draw_dot(bob, pos):
    bob.penup()
    bob.setpos(pos)
    bob.pendown()
    bob.dot()


A = (100, 100)
B = (-100, 100)
C = (-100, -100)
start = (0, 0)

bob = turtle.Turtle()
bob.speed('fastest')

def main():

    draw_dot(bob, A)
    draw_dot(bob, B)
    draw_dot(bob, C)
    draw_dot(bob, start)

    for i in range(10000):
        r = random.randint(1, 4)
        if r == 1:
            new_x = A[0] - bob.pos()[0]
            new_y = A[1] - bob.pos()[1]
        elif r == 2:
            new_x = B[0] - bob.pos()[0]
            new_y = B[1] - bob.pos()[1]
        else:
            new_x = C[0] - bob.pos()[0]
            new_y = C[1] - bob.pos()[1]

        new_pos = (bob.pos()[0] + (new_x / 2), bob.pos()[1] + (new_y / 2))
        draw_dot(bob, new_pos)

main()

turtle.done()