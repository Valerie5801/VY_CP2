#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle

#make a function with parameters of the recursion depth and triangle color and length of each side and the turtle that is used.:
def sip(depth, color, length, turt):
    turt.color(color)
    if depth == 0: #end when depth reaches zero
        return None
    for i in range(3): #draw the triangle.
        turt.left(120)
        turt.forward(length)
        sip(depth-1, color, length//2, turt) #make it call itself, halving the length to make the triangles inside the big triangle smaller.
    
    #draw triangle by rotating 120 degrees and moving the same distance for the sides

"""test_input = int(input("input a depth number: "))
t = turtle.Turtle()
t.goto(0, 0)
t.speed(0)
t.shape("turtle")

#test running it
sip(test_input, "blue", 400, t)
turtle.done()"""

#function that checks if the user typed in a valid color with parameters of the color and turtle:
def check_color(usr_color):
    test_turt = turtle.Screen()
    #try:
    try:
        #use .color() to check if it's valid
        test_turt.color(usr_color)
    #except, in case it doesn't work:
    except:
        #return False
        print("That isn't a valid color.")
        #test_turt.bye()
        return False
    #else, if it does work:
    else:
        #return True
        #test_turt.bye()
        return True