#VY 2nd Menu Actions for Word Counter
#import helper_functions_read
import helper_functions_read
#import time_clean_functions
import time_clean_functions

#this is where the functions that use other functions for their mechanics will be

#function for updating file path with parameter of the dictionary that holds all the file data:
def update_path(doc_info):
    #Ask the user for the specific file path
    new_path = input("Please type the EXACT relative path for the file: ")
    #Replace the old file path in the dictionary with the new one
    doc_info["Path"] = new_path
    #return the dictionary
    return doc_info

#function that shows the whole txt document to the user:
def show_doc():
    #try the following
    try:
        #open the txt document:
        with open("individual_projects/word counter/example_doc.txt", "r") as document:
            #make a list named content
            content = []
            #for loop here:
            for line in document:
                content.append(line.strip())
                #for each line in the txt document, append it to content
    #except:
    except:
        print("document not found")
        #show that the txt document doesn't work
    #else statement:
    else:
        #loop through content:
        for line in content:
            print(line)
            #print out each line

#function that lets the user add content to the document with parameter of the list that holds lines of the txt document in different values:
def add_content(doc_content):
    #Ask the user for what they want to add to the document, and tell them to press enter twice to stop editing (this allows the user to write on separate lines)
    print("Enter new content (press Enter twice when you're done.): ")
    new_content = input().splitlines()
    #split the user's input based off of different lines, and add each one to the list
    for line in new_content:
        doc_content.append(line)
    #return the list
    return doc_content