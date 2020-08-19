#!/usr/bin/env python3

import turtle

def square(len=100):
    turtle.forward(len)
    turtle.left(90)
    turtle.forward(len)
    turtle.left(90)
    turtle.forward(len)
    turtle.left(90)
    turtle.forward(len)
    turtle.left(90)

def Main():
    # do the main stuff
    for i in range(1,25):
        square(i)
        turtle.left(15)

if __name__ == '__main__':
    # do all the stuff; at a minimum, this will invoke Main()
    # if Main() not defined as fucntion, main body of program can go here
    Main()

    # maintain screen until the next keystroke
    input()
