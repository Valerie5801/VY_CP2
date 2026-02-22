#VY Functions for Reading and File Handling for Word Counter
#import time here
import datetime

#function for saving the txt document:         file_path is the path of the file that the user is currently editing.
def save_doc():
    try:
        with open("individual_projects/word counter/example_doc.txt", "r") as document:
            content = []
            for line in document:
                content.append(line.capitalize().strip())
    #open the txt document using r+ mode:
        #read each line and write it
        #make a list
        #go through the txt document and save each line as different values in the list
        #return the list
    except:
        print("file not found")
    else:
        return content

#function for rewriting the txt document with parameters of line_in, a list that has each line of the document as different values, and file_path:
def rewrite_doc(line_in):
    try:
        #open the txt document using mode w:
        with open("individual_projects/word counter/example_doc.txt", "w") as document:
            #clear the file
            document.truncate(0)
            #loop through line_in:
            for line in line_in:
                #Write each line on the text file.
                document.write(line)
    except:
        print("file not found")

#function that simply adds content to the txt document with parameters of added_lines:
def add_doc(added_lines):
    try:
        #open the txt document using mode a:
        with open("individual_projects/word counter/example_doc.txt", "a") as document:
            #loop through added_lines:
            for line in added_lines:
                document.write(line)
                #use .write to write each line.
    except:
        print("file not found")

#function for getting input for new content:
def new_cont():
    #Ask the user for their new content by using an input. Make sure it's in a pretty format.
    print("Enter new content (press enter twice to finish): ")
    lines = []
    while True:
        user_add = input()
        if user_add == "":   #allows user to go on new line and finish input when they enter on a new line
            break
        lines.append(user_add + "\n")
    #return this content.
    return "".join(lines)

#function that gets the word count of the TXT file. this uses parameter line_in, a list that has each line of the document as different values:
def get_word_count(line_in):
    #Make a variable called total_words and set it to 0
    total_words = 0
    #Loop through line_in:
    for line in line_in:
        counter_line = line.split()
        #Split each line and set it to counter_line
        #Add the length of counter_line to total_words.
        total_words += len(counter_line)
    #return total_words
    return total_words

#function just for getting the current time
def get_time():
    #First get the current time. Set it to last_edited.
    last_edit = datetime.datetime.now()
    return last_edit
