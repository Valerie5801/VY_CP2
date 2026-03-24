#VY 2nd User Menu for Geometry Calculator
#import actions
import action_funcs
#import helpers
import helpers

#main_menu function:
def main_menu():
    #run the function that saves the CSV to a list made of dictionaries. Set it to exist_shapes.
    exist_shapes = helpers.save_csv()
    #use exist_shapes as an argument needed for anything that needs to access it.
    if not exist_shapes:
        print("\nThere are currently no shapes that have been made.")
        #show that there are no shapes that have been made
    #while True loop:
    while True:
        #Show how many shapes have been created
        #let the user know what they can do:
            #1. create new shape
            #2. view all shapes
            #3. view a specific shape
            #4. Compare two shapes
            #5. Formula guide
            #6. Exit

        shape_count = helpers.count_shapes(exist_shapes)
        print(f"\n{shape_count} shapes have been made.")
        print("\nYou may: \n1. Create a new shape\n2. View all shapes\n3. Select a shape\n4. Compare two shapes\n5. See the formula guide\n6. Exit")

        #ask for the user's action as an input and set it to user_action
        user_action = input("\nWhat do you want to do?: ")
        
        #match user_action here:
        match user_action:
            #case 1:
            case "1":
                #run the create new shape function (from actions)
                new_shape = action_funcs.create_shape(exist_shapes)
                exist_shapes.append(new_shape)
                try:
                    exist_shapes.remove("placeholder")
                except:
                    pass
                print(f"{new_shape['Label']} has been created!")
                helpers.show_specific(new_shape)
            #case 2:
            case "2":
                #run the view shapes function (from actions)
                action_funcs.display_shapes(exist_shapes)
            #case 3:
            case "3":
                #ask the user what shapes they want to use
                #run the view specific function
                action_funcs.scale_shape(exist_shapes)
            #case 4:
            case "4":
                #check if there is more than one shape
                check_shape = False
                if shape_count > 1:
                    while not check_shape:
                        shape_one = input('\nWhat shape do you want the comparison to be based on/the first shape?(use the label name such as "Circle 1"): ')
                        for shape in exist_shapes:
                            if shape_one == shape["Label"]:
                                check_shape = True
                                first_shape = shape
                            else:
                                pass
                        if not check_shape:
                            print("That isn't an existing shape. Please use the label given to the shape.")
                        else:
                            break

                    check_shape = False
                    while not check_shape:
                        shape_two = input('What shape do you want to compare to/the second shape?(use the label name such as "Circle 1"): ')
                        for shape in exist_shapes:
                            if shape_two == shape["Label"]:
                                second_shape = shape
                                check_shape = True
                            else:
                                pass
                        if not check_shape:
                            print("That isn't an existing shape. Please use the label given to the shape.")
                        else:
                            #run the compare shapes function
                            action_funcs.compare_shapes(first_shape, second_shape)
                            break
                else:
                    print(f"Only {shape_count} shapes exist. You need at least two shapes to compare them.")
            #case 5:
            case "5":
                #run the formula guide function
                action_funcs.formula_guide()
            #case 6:
            case "6":
                #break
                break
            #case _:
            case _:
                #let the user know that what they put was not a valid option.
                print("That isn't something you can do.")

        #run the function that re-saves the CSV by using the list (from helpers)
        helpers.rewrite_csv(exist_shapes)