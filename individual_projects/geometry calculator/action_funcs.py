#VY 2nd Functions for each available thing that the user cna do in the meny for Geometry Calculator
#import helpers
#import shape_classes
import helpers
import shape_classes

#function for making a new shape:
def create_shape():
    #ask the user what shape they want
    print("Available shapes: \n\t-Rectangle \n\t-Square \n\t-Circle \n\t-Triangle")
    ask_shape = input("What shape do you want?")
    #ask them for the required measurements for each shape
    #make an object from the respective class of the shape that they chose. Append them to new_shape.
    #calculate the area and perimeter and append them to new_shape

    match ask_shape.capitalize().strip():
        case "Rectangle":
            print("What is the length of the rectangle?")
            rect_len = helpers.check_num()
            print("What is the width of the rectangle?")
            rect_height = helpers.check_num()
            return shape_classes.Rectangle(rect_len, rect_height)
        
        case "Square":
            print("What is the side of the square?")
            square_side = helpers.check_num()
            return shape_classes.Rectangle(square_side)
        
        case "Circle":
            print("What is the radius of the circle?")
            circ_radius = helpers.check_num()
            return shape_classes.Rectangle(circ_radius)
        
        case "Triangle":
            print("What is the base of the triangle?")
            tri_base = helpers.check_num()
            print("What is the first side of the triangle?")
            first_side = helpers.check_num()
            print("What is the second side of the triangle?")
            second_side = helpers.check_num()
            print("What is the height of the triangle?")
            tri_height = helpers.check_num()
            return shape_classes.Rectangle(tri_base, first_side, second_side, tri_height)
        
        case _:
            print("Sorry, that isn't an available shape.")


#function that shows all the shapes with perimeter of the existing shapes:
def display_shapes(exist_shapes):
    #loop through the list of dictionaries and print out in the dictionary
    pass


#function that lets the user do something with a specific shape:
def scale_shape(shape):
    #ask the user for the shape they want to view via label (the Circle #1, Circle #2, Rectangle #2 things)
    pass


#function that lets the user compare shapes:
def compare_shapes(first_shape, second_shape):
    pass


#function that shows a guide to the formulas:
def formula_guide():
    pass
    #ask the user what formulas they want to see. they can choose:
        #-All area formulas
        #-All perimeter formulas
        #-Rectangle formulas
        #-Square formulas
        #-Circle formulas
        #-Triangle formulas

    #Display the respective information depending on what they choose (for example if they chose area, show all the area formulas)