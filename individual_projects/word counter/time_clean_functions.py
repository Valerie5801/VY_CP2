#VY 2nd Time Functions for Word Counter
#import CSV here

#function that rewrites the word count and last edited to the doc_info CSV. This uses parameter of count_words:
    #First get the current time. Set it to last_edited.
    #try the following:
        #Open the CSV using write mode:
            #make a list of fieldnames consisting of Path and Word Count and Last Edited
            #make a variable named writer which uses csv.writer
            #first write the fieldnames
            #then write, on the same row, count_words and last_edited.   (don't write the path)
    #except statement here:
        #show that the CSV wasn't found

#function that saves the data from the CSV file into a dictionary:
    #try the following:
        #open doc_info.csv:
            #make an empty list to hold the dictionary info
            #use a for loop to make a dictionary
            #append the dictionary to movies
    #except statement here:
        #show that the CSV wasn't found
    #else:
        #return the dictionary

#function that shows the word count and the last updated time in a nice format:
    #try here:
        #Open the CSV using read mode:
            #read the CSV and get the next line
            #Make a dictionary named formatted_info
            #put the information for the word count and the last updated time, but skip the path.
    #except here:
        #show the CSV wasn't found
    #else:
        #return formatted_info