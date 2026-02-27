#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle

turt = turtle.Turtle()
turt.teleport(0, 0)
turt.speed(5)
turt.shape("turtle")
turt.penup()

#make a function with parameters of the recursion depth and triangle color and length of each side and the turtle that is used.:
def draw_triangle(depth, color, length, t):
    if depth == 0:
        for i in range(3):
            t.left(120)
            t.forward(length) 
        return None
    t.color(color)
    t.pendown()
    #draw the triangles. use loops so multiple of them will be inside each other
    def inter_tri(counter, lenth):
        t.left(120)
        t.forward(lenth*counter)
        counter *= 2
        last_pos = t.pos()
        distance = int(t.distance(last_pos))
            
        return inter_tri(counter, distance)
        
    double_count = 1
    for i in range(3):
        inter_tri(double_count, 10)

        
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
    
    draw_triangle(depth, color, length*2, t)
    #draw triangle by rotating 60 degrees and moving the same distance for the sides
    #return the recursion depth minus 1, the triangle color, and the length of the side divided by 2

#test_input = int(input("input a depth number: "))

#draw_triangle(4, "blue", 50, turt)

#basic triangle
turt.pendown()
for i in range(3):
    turt.left(120)
    turt.forward(50) 
turtle.done()