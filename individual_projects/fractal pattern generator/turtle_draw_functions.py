#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle

turt = turtle.Turtle()
turt.teleport(0, 0)
turt.speed(0)
turt.shape("turtle")
turt.penup()

#make a function with parameters of the recursion depth and triangle color and length of each side and the turtle that is used.:
def draw_triangle(depth, color, length, t):
    if depth == 0:
        print("we end") 
        return None
    turt.color(color)
    turt.pendown()
    #draw the triangles. use loops so multiple of them will be inside each other
    def inter_tri(counter):
        for i in range(3):
            t.left(120)
            t.forward(length*counter)
            counter *= 2
            return inter_tri(counter)
        
    double_count = 2
    for i in range(3):
        inter_tri(double_count)

    """for i in range(3):
        t.left(120)
        t.forward(length*8)
        for i in range(3):
            t.left(120)
            t.forward(length*4)
            for i in range(3):
                t.left(120)
                t.forward(length*2)
                for i in range(3):
                    t.left(120)
                    t.forward(length)"""
    depth -= 1
    return draw_triangle(depth, color, length*2, t)
    #draw triangle by rotating 60 degrees and moving the same distance for the sides
    #return the recursion depth minus 1, the triangle color, and the length of the side divided by 2

draw_triangle(4, "blue", 10, turt)
turtle.done()