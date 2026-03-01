#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle


#make a function with parameters of the recursion depth and triangle color and length of each side and the turtle that is used.:
def sip(depth, color, length, turt):
    turt.color(color)
    if depth == 0:
        return None
    for i in range(3):
        turt.left(120)
        turt.forward(length)
        sip(depth-1, color, length//2, turt)
    
    #draw triangle by rotating 120 degrees and moving the same distance for the sides
    #return the recursion depth minus 1, the triangle color, and the length of the side divided by 2

test_input = int(input("input a depth number: "))
t = turtle.Turtle()
t.goto(0, 0)
t.speed(0)
t.shape("turtle")

#test running it
sip(test_input, "blue", 400, t)
turtle.done()