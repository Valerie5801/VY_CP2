#VY 2nd Main Menu for fractal pattern generator
#import turtle_draw_functions
from turtle_draw_functions import sip
import turtle

#function named "main_menu":
def main_menu():
    #While true loop:
    while True:
        #ask the user if they want to draw a siperniski triangle or exit out of the program
        print("You can: \n1. Draw a Siperniski Triangle \n2. Exit")
        user_action = input("What do you want to do?(1/2): ")
        #If they want to draw a siperniski triangle:
        if user_action == "1":

            #ask them for the depth they want. Tell them that it is reccommended they set a depth less than 8.
            while True:
                tri_depth = input("Depth for the triangle (as a number): ")
                if not tri_depth.isnumeric():
                    print("That isn't a number. Please try again.")
                else:
                    tri_depth = int(tri_depth)

            #Ask them for the color they want the triangle to be.
            tri_color = input("Type a color for the triangle: ")

            #set up turtle here
            t = turtle.Turtle()
            t.hideturtle()
            t.speed(0)

            #run the sip function from turtle_draw_functions
            sip(tri_depth, tri_color, 400, t)
        #Else:
        else:
            break
            #break out of the program

main_menu()