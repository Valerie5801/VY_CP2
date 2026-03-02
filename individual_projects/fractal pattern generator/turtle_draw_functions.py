#VY 2nd Turtle functions for Fractal Pattern Generator
#import turtle
import turtle

#make a function with parameters of the recursion depth and triangle color and length of each side and the turtle that is used.:
def sier(depth, color, length, turt):
    turt.color(color)
    if depth == 0: #end when depth reaches zero
        return None
    for i in range(3): #draw the triangle.
        turt.left(120)
        turt.forward(length)
        sier(depth-1, color, length//2, turt) #make it call itself, halving the length to make the triangles inside the big triangle smaller.
    
    #draw triangle by rotating 120 degrees and moving the same distance for the sides

#function that checks if the user typed in a valid color with a parameter of the color:
def check_color(usr_color):
    test_screen = turtle.Screen()
    #try:
    try:
        #try using usr_color for the background to see if its a valid color
        test_screen.bgcolor(usr_color)
        test_screen.bgcolor("white") #set it back to white after check is done.
    #except, in case it doesn't work:
    except:
        #return False
        print("That isn't a valid color.")
        return False
    #else, if it does work:
    else:
        #return True
        return True