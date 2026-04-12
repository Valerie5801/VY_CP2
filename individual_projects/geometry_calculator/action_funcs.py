#VY 2nd Functions for each available thing that the user cna do in the meny for Geometry Calculator
#import helpers
#import shape_classes
from . import helpers
from . import shape_classes
import time

#function for making a new shape:
def create_shape(shapes):
    label_num = 0
    print("When asked about the dimensions, please type the values of the measurements.")
    #ask the user what shape they want
    print("\nAvailable shapes: \n\t-Rectangle \n\t-Square \n\t-Circle \n\t-Triangle")
    ask_shape = input('What shape do you want?(write like "Rectangle"): ')
    #ask them for the required measurements for each shape
    #make an object from the respective class of the shape that they chose. Append them to new_shape.
    #calculate the area and perimeter and append them to new_shape
    
    match ask_shape.capitalize().strip():
        case "Rectangle":
            print("What is the length of the rectangle?")
            rect_len = helpers.check_num()
            print("What is the width of the rectangle?")
            rect_height = helpers.check_num()
            rectangle = shape_classes.Rectangle(rect_len, rect_height)
            rectangle.calc_peri()
            rectangle.calc_area()
            rectangle = rectangle.save_info()
            label_num = helpers.count_specific(shapes, "Rectangle")
            rectangle["Label"] = f"Rectangle {label_num}"
            return rectangle
        
        case "Square":
            print("What is the side length of the square?")
            square_side = helpers.check_num()
            square = shape_classes.Square(square_side)
            square.calc_peri()
            square.calc_area()
            square = square.save_info()
            label_num = helpers.count_specific(shapes, "Square")
            square["Label"] = f"Square {label_num}"
            return square
        
        case "Circle":
            print("What is the radius of the circle?")
            circ_radius = helpers.check_num()
            circle = shape_classes.Circle(circ_radius)
            circle.calc_peri()
            circle.calc_area()
            circle = circle.save_info()
            label_num = helpers.count_specific(shapes, "Circle")
            circle["Label"] = f"Circle {label_num}"
            return circle
        
        case "Triangle":
            print("What is the base of the triangle?")
            tri_base = helpers.check_num()
            print("What is the left side length of the triangle?")
            first_side = helpers.check_num()
            print("What is the right side length of the triangle?")
            second_side = helpers.check_num()
            print("What is the height of the triangle?")
            tri_height = helpers.check_num()
            triangle = shape_classes.Triangle(tri_base, first_side, second_side, tri_height)
            triangle.calc_peri()
            triangle.calc_area()
            triangle = triangle.save_info()
            label_num = helpers.count_specific(shapes, "Triangle")
            triangle["Label"] = f"Triangle {label_num}"
            return triangle
        
        case _:
            print("Sorry, that isn't an available shape.")



#function that shows all the shapes with parameter of the existing shapes:
def display_shapes(shapes):
    #loop through the list of dictionaries and print out in the dictionary
    if not shapes:
        print("No shapes have been made yet.")
        return
    print("\nShape Library:")
    for shape in shapes:
        helpers.show_specific(shape)
        print("")


#function for removing a shape:
def remove_shape(shapes):
    found_shape = ""
    #display all the shapes using display_shapes
    display_shapes(shapes)
    #ask the user what shape they want to remove via label.
    remove_shape = input("Type the label of the shape you want to remove: ")
    #loop through the dictionary and see if it exists
    for shape in shapes:
        if remove_shape.strip().lower() == shape['Label'].strip().lower():
            found_shape = shape
        else:
            pass

    if found_shape:
        print(f"{found_shape['Label']} has been successfully removed.")
        shapes = [shape for shape in shapes if shape['Label'] != found_shape['Label']]
    else:
        print("That shape doesn't exist.")

    return shapes

    #if it does, remove it from the shapes and tell the user it has been removed
    #if it doesn't, say that the label doesn't exist.


#function that lets the user do something with a specific shape:
def scale_shape(shapes):
    shape_exist = False
    while not shape_exist:
        #ask the user for the shape they want to view via label (the Circle #1, Circle #2, Rectangle #2 things)
        print('\nPlease type in the label, such as "Circle 1" or "Rectangle 2". To exit, type "exit"')
        show_shape = input('What is the shape you want to look at?: ')
        if show_shape.strip().lower() == "exit":
            return
        for shape in shapes:
            if show_shape.strip().lower() == shape["Label"].strip().lower():
                shape_exist = True
                found_shape = shape
                break
        if not shape_exist:
            print("That shape doesn't exist. Please try again.")
    #show the shape
    helpers.show_specific(found_shape)

    #ask the user if they want to scale it
    while True:
        ask_scale = input("\nDo you want to scale(multiplying a shape's dimensions by a scale factor) the shape?(type in y/n): ")
        #if they do:
            #run the scale_shape function from helpers
            #print the area and perimeter from the scale_shape function
        #if they don't:
            #break
        if ask_scale.strip().lower() == "y":
            while True:
                print("Decimals are allowed.")
                scale_fact = input("By what number do you want to scale by?: ")
                try:
                    scale_fact = float(scale_fact)
                    break
                except:
                    print("That isn't a number.")
            helpers.scale_shape(found_shape, scale_fact)
        elif ask_scale == "n":
            break
        else:
            print("That isn't an option.")



#function that lets the user compare shapes:
def compare_shapes(first_shape, second_shape):
    #ask the user in what way they want to compare it (either area or perimeter)
    is_greater = False
    while True:
        compare_how = input('\nHow do you want to compare them?(by Area or Perimeter. Type "exit" to exit): ')
        try:
            compare_how = compare_how.strip().capitalize()
        except:
            print("That isn't a word.")
            return
        #run the respective function
        #if it results in true, then say that the first shape's area/perimeter is greater than the second shape's area
        #if it results in false, then say that the first shape's area/perimeter is less than the second shape's area/perimeter
        #if it results in None, then say that their areas/perimeters are equal
        if compare_how == "Exit":
             return

        match compare_how:
            case "Area":
                is_greater = helpers.area_is_greater(first_shape["Area"], second_shape["Area"])
                break
            case "Perimeter":
                is_greater = helpers.peri_is_greater(first_shape["Perimeter"], second_shape["Perimeter"])
                break
            case _:
                print("That isn't an option. Please type either Area or Perimeter")

    print("Comparing shapes...")
    time.sleep(1)

    if is_greater:
        print(f"{first_shape['Label']} has a LARGER {compare_how} than {second_shape['Label']}.")
    elif is_greater is None:
        print(f"{first_shape['Label']} has THE SAME {compare_how} as {second_shape['Label']}.")
    elif not is_greater:
        print(f"{first_shape['Label']} has a SMALLER {compare_how} than {second_shape['Label']}.")



#function that shows a guide to the formulas:
def formula_guide():
    #ask the user what formulas they want to see. they can choose:
        #-All area formulas
        #-All perimeter formulas
        #-Rectangle formulas
        #-Square formulas
        #-Circle formulas
        #-Triangle formulas

    #Display the respective information depending on what they choose (for example if they chose area, show all the area formulas)
    rectangle_forms = {
        "Area": "Length x Width",
        "Perimeter": "2(Length + Width)"
    }

    square_forms = {
        "Area": "Side\u00B2",
        "Perimeter": "4 x Side"
    }

    circle_forms = {
        "Area": "πr\u00B2",
        "Perimeter": "2πr"
    }

    tri_forms = {
        "Area": "Base x Height x 0.5",
        "Perimeter": "Base + First Side + Second Side"
    }


    print("This is the formula guide.")
    while True:
        print("You may: \n1. View all Area formulas\n2. View all Perimeter formulas\n3. View the Rectangle formulas\n4. View the Square formulas\n5. View the Circle formulas\n6. View the Triangle formulas\n7. Exit")
        print("Please type in the numbers to select your option (type in 1 for Area formulas, for example).")
        user_view = input("\nWhat would you like to do?: ")

        match user_view:
            case "1":
                print("\nArea formulas:")
                print(f"\tRectangle Area: {rectangle_forms['Area']}")
                print(f"\tSquare Area: {square_forms['Area']}")
                print(f"\tCircle Area: {circle_forms['Area']}")
                print(f"\tTriangle Area: {tri_forms['Area']}")
            case "2":
                print("\nPerimeter formulas:")
                print(f"\tRectangle Perimeter: {rectangle_forms['Perimeter']}")
                print(f"\tSquare Perimeter: {square_forms['Perimeter']}")
                print(f"\tCircle Perimeter: {circle_forms['Perimeter']}")
                print(f"\tTriangle Perimeter: {tri_forms['Perimeter']}")
            case "3":
                print("\nRectangle formulas:")
                print(f"\tArea: {rectangle_forms['Area']}")
                print(f"\tPerimeter: {rectangle_forms['Perimeter']}")
            case "4":
                print("\nSquare formulas:")
                print(f"\tArea: {square_forms['Area']}")
                print(f"\tPerimeter: {square_forms['Perimeter']}")
            case "5":
                print("\nCircle formulas:")
                print(f"\tArea: {circle_forms['Area']}")
                print(f"\tPerimeter: {circle_forms['Perimeter']}")
            case "6":
                print("\nTriangle formulas:")
                print(f"\tArea: {tri_forms['Area']}")
                print(f"\tPerimeter: {tri_forms['Perimeter']}")
            case "7":
                break
            case _:
                print("That isn't an option, please try again.")