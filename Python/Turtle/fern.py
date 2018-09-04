import sys, pygame, random
from pygame.locals import *

pygame.init()

WIDTH  = 400
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Barnsley\'s Fern')

####------Colours------####
DARKGREEN  = (  0,  0,   0)
LIGHTGREEN = (  0, 166,  17)
####-------------------####

def convert_point(tup):
    tup    = list(tup)
    tup[0] = (tup[0] + 2.5)  * ((WIDTH  - 20) /  5)
    tup[1] = HEIGHT - tup[1] * ((HEIGHT - 20) / 10) - 10

    return tuple(tup)

def f1(point):
    x =  0
    y =  0.16 * point[1]

    return x, y

def f2(point):
    x =  0.85 * point[0] + 0.04 * point[1]
    y = -0.04 * point[0] + 0.85 * point[1] + 1.6

    return x, y

def f3(point):
    x =  0.20 * point[0] - 0.26 * point[1]
    y =  0.23 * point[0] + 0.22 * point[1] + 1.6

    return x, y

def f4(point):
    x = -0.15 * point[0] + 0.28 * point[1]
    y =  0.26 * point[0] + 0.24 * point[1] + 0.44

    return x, y

def main():
    point = (0, 0)
    SCREEN.fill(DARKGREEN)

    while True:
        SCREEN.fill(LIGHTGREEN, (convert_point(point), (1, 1)))

        rand = random.random()
        if   rand <= 0.01: point = f1(point)
        elif rand >  0.01 and rand <= 0.86: point = f2(point)
        elif rand >  0.86 and rand <= 0.93: point = f3(point)
        elif rand >  0.95 and rand <= 1.00: point = f4(point)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()