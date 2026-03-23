#VY 2nd Functions for each available thing that the user cna do in the meny for Geometry Calculator
#import helpers
#import shape_classes
import helpers
import shape_classes

#function for making a new shape:
def create_shape(shapes):
    label_num = 0
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


#function that shows all the shapes with perimeter of the existing shapes:
def display_shapes(shapes):
    #loop through the list of dictionaries and print out in the dictionary
    if not shapes:
        print("No shapes have been made yet.")
        return
    
    for shape in shapes:
        print(f"\n{shape['Label']}")

        #print specific labels for each measurement for each shape
        if shape["Type"] == "Rectangle":
            print(f"Length: {shape['First Measurement']} units")
            print(f"Width: {shape['Second Measurement']} units")
        elif shape["Type"] == "Square":
            print(f"Side: {shape['First Measurement']} units")
        elif shape["Type"] == "Circle":
            print(f"Radius: {shape['First Measurement']} units")
        elif shape["Type"] == "Triangle":
            print(f"Base: {shape['First Measurement']} units")
            print(f"Left Side: {shape['Second Measurement']} units")
            print(f"Right: {shape['Third Measurement']} units")
            print(f"Height: {shape['Fourth Measurement']} units")

        print(f"Perimeter: {shape['Perimeter']} units")
        print(f"Area: {shape['Area']} units\u00B2")


#function that lets the user do something with a specific shape:
def scale_shape(shapes):
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