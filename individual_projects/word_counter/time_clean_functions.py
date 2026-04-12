#VY 2nd Time Functions for Word Counter
#import CSV here
import csv

#function that rewrites the word count and last edited to the doc_info CSV. This uses parameter of doc_info:
def edit_info(doc_info):
    #try the following:
    try:
        #Open the CSV using write mode:
        with open("individual_projects/word counter/doc_info.csv", "w", newline='') as csvfile:
            #make a list of fieldnames consisting of Path and Word Count and Last Edited
            fieldnames = ["Path", "Word Count", "Last Edited"]
            #make a variable named writer
            writer = csv.DictWriter(csvfile, fieldnames)
            #first write the fieldnames
            writer.writeheader()
            #then write all the info on the same row
            writer.writerows(doc_info)
    #except statement here:
    except:
        print("CSV not found")
        #show that the CSV wasn't found

#function that saves the data from the CSV file into a dictionary:
def save_info():
    #try the following:
    try:
        #open doc_info.csv:
        with open("individual_projects/word counter/doc_info.csv", "r", newline='') as csvfile:
            read_info = csv.reader(csvfile)
            next_line = next(read_info)
            #make an empty list to hold the dictionary info
            dict_info = []
            #use a for loop to make a dictionary
            for line in read_info:
                dict_info.append(
                    {
                        next_line[0]: line[0],
                        next_line[1]: line[1],
                        next_line[2]: line[2]
                    }
                )
            #append the dictionary to movies
    #except statement here:
    except:
        print("CSV not found")
        #show that the CSV wasn't found
    #else:
    else:
        return dict_info
        #return the dictionary

#function that shows the word count and the last updated time in a nice format with parameter doc_info:
def nice_print(doc_info):
    #concatenate the word count and last edited time into a nice format and set it to variable format_info
    #return format_info
    format_info = "Word Count: " + doc_info["Word Count"] + "\nLast Edited: " + doc_info["Last Edited"]
    return format_info