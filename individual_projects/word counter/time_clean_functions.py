#VY 2nd Time Functions for Word Counter
#import CSV here

#function that saves the word count and last edited to the doc_info CSV. This uses parameter of count_words:
    #First get the current time. Set it to last_edited.
    #try the following:
        #Open the CSV using write mode:
            #make a list of fieldnames consisting of Path and Word Count and Last Edited
            #make a variable named writer which uses csv.writer
            #first write the fieldnames
            #then write, on the same row, count_words and last_edited.   (don't write the path)
    #except statement here:
        #show that the CSV wasn't found