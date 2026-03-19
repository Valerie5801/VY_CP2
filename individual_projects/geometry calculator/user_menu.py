#VY 2nd User Menu for Geometry Calculator
#import actions
#import helpers

#main_menu function:
    #run the function that saves the CSV to a list made of dictionaries. Set it to exist_shapes.
    #use exist_shapes as an argument needed for anything that needs to access it.
    #while True loop:
        #Show how many shapes have been created
        #let the user know what they can do:
            #1. create new shape
            #2. view all shapes
            #3. view a specific shape
            #4. Compare two shapes
            #5. Formula guide
            #6. Exit

        #ask for the user's action as an input and set it to user_action
        
        #match user_action here:
            #case 1:
                #run the create new shape function (from actions)
            #case 2:
                #run the view shapes function (from actions)
            #case 3:
                #run the view specific function
            #case 4:
                #run the compare shapes function
            #case 5:
                #run the formula guide function
            #case 6:
                #break
            #case _:
                #let the user know that what they put was not a valid option.

        #run the function that re-saves the CSV by using the list (from helpers)