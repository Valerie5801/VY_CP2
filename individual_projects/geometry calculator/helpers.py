#VY 2nd Helper Functions for Geometry Calculator
#import CSV
import csv

#function to save the CSV for first time when program is ran
def save_csv():
    #try the following:
    try:
        #open the provided movies list and set the mode to "r" for reading as sample:
        with open("individual_projects\\geometry calculator\\docs\\shapes.csv", mode= "r") as sample:
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
                        next_item[4]: line[4]
                    }
                )
                #append the dictionary with the respective information (found using index values)
    #except statement here if the try doesn't work:
    except:
        print("The CSV doesn't exist.")
        #show that the CSV doesn't exist.
        #Return None
        return None
    #else statement:
    else:
        #Return library
        return store_shapes
    

#function for rewriting the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv(shapes):
    with open("individual_projects//updated personal library//new_personal_library.csv", "w", newline='') as csvfile:
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
    pass


#function to scale the shapes with 