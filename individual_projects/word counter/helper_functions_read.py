#VY Functions for Reading and File Handling for Word Counter
#import time here
#import csv here
#import time_clean_functions here

#function for saving the txt document with parameter of file_path:         file_path is the path of the file that the user is currently editing.
    #open the txt document using r+ mode:
        #read each line and write it
        #make a list
        #go through the txt document and save each line as different values in the list
        #return the list

#function for rewriting the txt document with parameters of line_in, a list that has each line of the document as different values, and file_path:
    #open the txt document using a mode:
        #clear the file
        #loop through line_in:
            #Write each line on the text file.
            #when the line is done, make a space.

#function for getting input for new content:
    #Ask the user for their new content by using an input. Make sure it's in a pretty format.
    #Print that the content was added successfully.
    #return this content.

#function that gets the word count of the TXT file. this uses parameter line_in, a list that has each line of the document as different values:
    #Make a variable called total_words and set it to 0
    #Loop through line_in:
        #Split each line and set it to counter_line
        #Add the length of counter_line to total_words.
    #return total_words

#function that shows the word count and the last updated time in a nice format with parameters of the time:
    #try here:
        #Open the CSV using read mode:
            #read the CSV and get the next line
            #Make a dictionary named formatted_info
    #except here:
        #show the CSV wasn't found
    #else:
        #return formatted_info

#