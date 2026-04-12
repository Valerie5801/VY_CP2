#VY 2nd Main Menu for fractal pattern generator
#import turtle_draw_functions
from . import turtle_draw_functions
import turtle

#function named "main_menu":
def main_menu():
    t = None  # Initialize t before the loop
    #While true loop:
    while True:
        #ask the user if they want to draw a siperniski triangle or exit out of the program
        print("\nYou can: \n1. Draw a Sierpniski Triangle \n2. Exit")
        user_action = input("What do you want to do?(1/2): ")
        #If they want to draw a siperniski triangle:
        if user_action == "1":

            #ask them for the depth they want. Tell them that max is 5
            while True:
                tri_depth = input("\nDepth for the triangle (as a number. max is 5): ")
                if not tri_depth.isnumeric():
                    print("That isn't a number. Please try again.")
                elif int(tri_depth) > 5:
                    print("That's above 5!")
                else:
                    tri_depth = int(tri_depth)
                    break

            color_valid = False
            while not color_valid:
                #Ask them for the color they want the triangle to be.
                tri_color = input("Type a color for the triangle: ")
                color_valid = turtle_draw_functions.check_color(tri_color)

            #set up turtle here
            t = turtle.Turtle()
            screen = turtle.Screen()
            screen.title("Siperniski Fractal")
            screen.tracer(0) #make the drawing instant

            #put the window in front
            try:
                screen._root.attributes('-topmost', True)
            except Exception:
                pass


            t.hideturtle()
            t.speed(0)
            t.penup()
            t.goto(180, -150)
            t.pendown()

            #run the sip function from turtle_draw_functions
            turtle_draw_functions.sier(tri_depth, tri_color, 400, t)
            screen.update()

            #wait for user to press enter when program done drawing to close window
            input("Press enter to close the window.")

            #clear the screen and put it behind vscode window
            try:
                screen._root.lower()
                turtle.clearscreen()
            except:
                pass

        #Else:
        elif user_action == "2":
            #remove turtle if it was created
            if t is not None:
                t.clear()
            break
            #break out of the program
        
        else: #stupid proofing
            print("That isn't an option. Please try again.")