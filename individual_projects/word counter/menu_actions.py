#VY 2nd Menu Actions for Word Counter
#import helper_functions_read
import helper_functions_read
#import time_clean_functions
import time_clean_functions

#this is where the functions that use other functions for their mechanics will be

#function for updating file path with parameter of the dictionary that holds all the file data:
def update_path()
    #Ask the user for the specific file path
    #Replace the old file path in the dictionary with the new one
    #return the dictionary

#function that shows the whole txt document to the user:
    #try the following
        #open the txt document:
            #make a list named content
            #for loop here:
                #for each line in the txt document, append it to content
    #except:
        #show that the txt document doesn't work
    #else statement:
        #loop through content:
            #print out each line

#function that lets the user add content to the document with parameter of the list that holds lines of the txt document in different values:
    #Ask the user for what they want to add to the document, and tell them to press enter twice to stop editing (this allows the user to write on separate lines)
    #split the user's input based off of different lines, and add each one to the list
    #return the list