#!/usr/bin/env python3

def main():
    # do the main stuff

    import turtle

    for i in range(1, 100):
        turtle.forward(2*i)
        turtle.left(90)
    turtle.penup()
    turtle.home()
    input()

if __name__ == '__main__':
    # do all the stuff; at a minimum, this will invoke Main()
    # if Main() is not defined as fucntion, that block can just go here
    main()
