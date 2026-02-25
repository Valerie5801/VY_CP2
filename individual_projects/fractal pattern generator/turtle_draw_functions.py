#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle

turt = turtle.Turtle()
turt.teleport(0, 0)

#make a function with parameters of the recursion depth and triangle color and length of each side:
def draw_triangle(depth, color, length):
    if depth == 0:
        print("we end") 
        return None
    turt.shape("turtle")
    turt.penup()
    turt.color(color)
    turt.pendown()
    if depth%2 != 0:
        #turt.right(120)
        #turt.forward(length/2)
        for i in range(3):
            turt.right(120)
            turt.forward(length)
    else:
        for i in range(3):
            turt.left(120)
            turt.forward(length)
    depth -= 1
    turt.right(120)
    turt.forward(60)
    return draw_triangle(depth, color, length/2)
    #draw triangle by rotating 60 degrees and moving the same distance for the sides
    #return the recursion depth minus 1, the triangle color, and the length of the side divided by 2

draw_triangle(4, "blue", 200)
turtle.done()