#VY Functions for Reading and File Handling for Word Counter
#import time here
import datetime
from pathlib import Path

#function for saving the txt document:         file_path is the path of the file that the user is currently editing.
def save_doc():
    try:
        doc_path = Path(__file__).parent / "example_doc.txt"
        with open(doc_path, "r") as document:
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

#function for rewriting the txt document with completely new content from the user:
def rewrite_doc():
    #Ask the user for what they want to write to replace the entire document
    print("Enter new content to replace the entire document (press Enter twice when you're done.): ")
    # Read multiple lines until the user enters a blank line.
    new_lines = []
    while True:
        line = input()
        if line == "":
            break
        new_lines.append(line)
    
    try:
        #open the txt document using mode r+:
        doc_path = Path(__file__).parent / "example_doc.txt"
        with open(doc_path, "r+") as document:
            #clear the file
            document.truncate(0)
            #loop through new_lines:
            for line in new_lines:
                #Write each line on the text file.
                # Ensure each written line ends with a newline.
                if line.endswith("\n"):
                    document.write(line)
                else:
                    document.write(line + "\n")
    except:
        print("file not found")

#function that simply adds content to the txt document with parameters of added_lines:
def add_doc(added_lines):
    try:
        #open the txt document using mode a:
        doc_path = Path(__file__).parent / "example_doc.txt"
        with open(doc_path, "a") as document:
            #loop through added_lines:
            for line in added_lines:
                # Write each line and ensure it ends with a newline so text doesn't concatenate.
                if line.endswith("\n"):
                    document.write(line)
                else:
                    document.write(line + "\n")
                #use .write to write each line.
    except:
        print("file not found")

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
