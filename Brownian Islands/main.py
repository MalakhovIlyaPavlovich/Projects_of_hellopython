from turtle import penup, pendown, goto, exitonclick, speed
from random import random
from math import sqrt

def brown(x0, y0, x1, y1, disp, p, n=8, m=200):
    if n == 0:
        penup()
        goto(x0*m - m/2, y0*m - m/2)
        pendown()
        goto(x1*m - m/2, y1*m - m/2)
        return
    xm = (x0 + x1) / 2
    ym = (y0 + y1) / 2
    deltax = random()*sqrt(disp)
    deltay = random()*sqrt(disp)
    brown(x0, y0, xm+deltax, ym+deltay, disp/p, p, n-1)
    brown(xm+deltax, ym+deltay, x1, y1, disp/p, p, n-1)


def main():
    h = 0.5 # float(input())
    a = 2**(2*h)
    disp = 0.1

    speed(0)
    brown(-0.2, 0, 0.8, 1, disp, a)
    brown(0.8, 1, 1, 0.5, disp, a)
    brown(1, 0.5, 0.5, 0.1, disp, a)
    brown(0.5, 0.1, -0.2, 0, disp, a)
    exitonclick()


if __name__ == '__main__':
    main()