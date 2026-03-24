#VY 2nd Helper Functions for Geometry Calculator
#import CSV
import csv
import math

#function to save the CSV for first time when program is ran
def save_csv():
    #try the following:
    try:
        #open the provided movies list and set the mode to "r" for reading as sample:
        with open("individual_projects/geometry calculator/docs/shapes.csv", mode= "r") as sample:
            #read sample and set it to the variable read_list
            read_list = csv.reader(sample)
            #make a variable that grabs the next value in the CSV reader
            next_item = next(read_list)
            #make an empty list called "store_shapes"
            store_shapes = []
            #Use a for loop here to make a dictionary:
            for line in read_list:
                store_shapes.append(
                    {
                        next_item[0]: line[0],
                        next_item[1]: line[1],
                        next_item[2]: line[2],
                        next_item[3]: line[3],
                        next_item[4]: line[4],
                        next_item[5]: line[5],
                        next_item[6]: line[6],
                        next_item[7]: line[7]
                    }
                )
                #append the dictionary with the respective information (found using index values)
    #except statement here if the try doesn't work:
    except:
        print("The CSV doesn't exist.")
        #show that the csv doesn't exist
        #Return None
        return []
    #else statement:
    else:
        #Return store_shapes
        return store_shapes
    


#function for rewriting the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv(shapes):
    with open("individual_projects/geometry calculator/docs/shapes.csv", "w", newline='') as csvfile:
        fieldnames = ['Type', 'Label', 'First Measurement', 'Second Measurement', 'Third Measurement', 'Fourth Measurement', 'Perimeter', 'Area']
        writer = csv.DictWriter(csvfile, fieldnames)   #read through dictionary and write each row as a new thing in the CSV
        writer.writeheader()
        writer.writerows(shapes)



#function for stupid-proofing with numbers:
def check_num():
    #while True loop:
    while True:
        #get an input from the user
        user_num = input("Type here: ")
        #if the input is not a number, ask them again
        if not user_num.isnumeric():
            print("That isn't a number. Please try again.")
        #if it is a number, break out of the loop
        else:
            break
    #return the input
    return float(user_num)
    


#function to count the shapes
def count_shapes(shapes):
    #count how many items are in the list
    counter = 0
    for shape in shapes:
        counter += 1
    return counter



#function to count a specific type of shape
def count_specific(shapes, type):
    count = 0
    for shape in shapes: #loop through the shapes
        if shape["Type"] == type: #check if the type of the shape matches the given type
            count += 1 #add one to the counter if so
    return count+1 #add 1 because this will become the label for the shape



#function to scale the shapes
def scale_shape(shape, scale_factor):
    area = 0
    perimeter = 0
    #multiply the measurements of the shape by the scale factor.
    new_first = shape["First Measurement"] * scale_factor
    new_second = shape["Second Measurement"] * scale_factor
    new_third = shape["Third Measurement"] * scale_factor
    new_fourth = shape["Fourth Measurement"] * scale_factor
    #find the area. use an if/else statement to get the different areas for each shape.
    if shape["Type"] == "Rectangle":
        area = new_first * new_second
    elif shape["Type"] == "Square":
        area = new_first**2
    elif shape["Type"] == "Circle":
        area = (new_first**2)*math.pi
    elif shape["Type"] == "Triangle":
        area = new_first * new_fourth * 0.5

    #find the perimeter. Just add all of the measurements together. (it will be the same for al shapes except Circle)

    if shape["Type"] == "Circle":
        perimeter = new_first*2*math.pi
    else:
        perimeter = new_first + new_second + new_third + new_fourth

    print(f"After scaling all of {shape["Label"]}'s measurements by {scale_factor}...")
    print(f"The new Area is {area}")
    print(f"The new Perimeter is {perimeter}")



#function to show a specific shape
def show_specific(shape):
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



#function to compare areas
def area_is_greater(first_area, second_area):
    #get the areas of the first and second shapes.
    #compare their values.
    #if the first shape's area is greater than the second shape's area:
    if first_area > second_area:
        #return true
        return True
    #if the second shape's area is greater than the first shape's area:
    elif first_area < second_area:
        #return false
        return False
    else: #failsafe in case they are the same
        return None



#function to compare perimeters
def peri_is_greater(first_peri, second_peri):
    #get the perimeters of the first and second shapes
    #compare their values
    #if the first shape's perimeter is greater than the second shape's perimeter:
    if first_peri > second_peri:
        #return true
        return True
    #else:
    elif first_peri < second_peri:
        #return false
        return False
    else: #failsafe
        return None