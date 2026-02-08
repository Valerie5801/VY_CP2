#VY 2nd Movie Recommender
#import csv here
import csv

#Function that saves the CSV file:
def save_csv():
    #try the following:
    try:
        #open the provided movies list and set the mode to "r" for reading as mov_list:
        with open("individual_projects/Movies list - Sheet1.csv", mode= "r") as sample:
            #read mov_list and set it to the variable read_list
            read_list = csv.reader(sample)
            #make a variable that grabs the next value in the CSV reader
            next_item = next(read_list)
            #make an empty list called "movies"
            movies = []
            #Use a for loop here to make a dictionary:
            for line in read_list:
                movies.append(
                    {
                        next_item[0]: line[0],
                        next_item[1]: line[1],
                        next_item[2]: line[2],
                        next_item[3]: line[3],
                        next_item[4]: line[4],
                        next_item[5]: line[5]
                    }
                )
                #append the dictionary with the respective information (found using index values)
    #except statement here if the try doesn't work:
    except:
        print("The CSV doesn't exist.")
        #show that no movies were found
        #Return None
        return None
    #else statement:
    else:
        #Return movies
        return movies

#Function that gets asks user what filters they want to apply:
    #Print the available filters to apply (and let them know it has to be separated with commas with no spaces.)
    #Genre is 1, Director is 2, Actor is 3, Length is 4.
    #Ask the user what filters they want to apply (via corresponding numbers).
    #Stupid proof here incase the user doesn't type something that is recognizeable by the program.
    #Return the filters that the user wants to apply

#Function that gets user input with parameter of the filters that the user wants (as numbers 1-4):
    #Make a list named "requirements". This will be used as the list for the filters that should be applied when searching for movies.
    #If 1 is in the string of filters that the user wants:
        #Ask the user for the genre they want and provide an example of how it should be formatted.
        #Append this to requirements
    #If 2 is in the string of filters that the user wants:
        #Ask the user of the name of the director, at least the first name.
        #Append this to requirements
    #If 3 is in the string of filters that the user wants:
        #Ask for one name of an actor they want to find movies about.
        #Append this to requirements.
    #If 4 is in the string of filters that the user wants:
        #Ask the user if they want to put the direct length of the movie or provide a range of movie lengths
        #If the user wants to put the direct length of the movie:
            #Ask the user for how many hours are in the movie
            #Ask the user for how many minutes are in the movie
            #Stupid proof it and make sure both values are numerical.
            #Multiply the hours by two, and add it to the amount of minutes to get the total time.
            #Append this to requirements
        #Or if the user wants to provide a range of length movies:
            #Ask the user for the minimum length in minutes
            #Ask the user for the maximum length in minutes
            #Put these two numbers into a list with minimum coming first. Then append this list to requirements.
    #Return requirements

#Helper function that filters by genre and has parameters of the dictionary or list of movies and the name of the genre that the user typed in:
    #Dictionary for the movies that qualify the filter requirements.
    #for loop that loops through the genres in the movie dictionary:
        #Check if that value matches the genre that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements

#Helper function that filters by directors and has parameters of the dictionary or list of movies and the name of the director that the user typed in:
    #Dictionary for the movies that qualify the filter requirements.
    #for loop that loops through the directors in the movie dictionary:
        #Check if that value matches the director that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements

#Helper function that filters by important actors and has parameters of the dictionary or list of movies and the name of the important actor(s) that the user typed in:
    #Dictionary for the movies that qualify the filter requirements.
    #for loop that loops through the important actors in the movie dictionary:
        #Loop here again to make sure all important actors are checked if there are multiple:
            #Check if that value matches the genre that the user chose.
            #If it does:
                #Add it to the dictionary
    #Return the dictionary for movies that met the requirements

#Helper function that filters by length and has parameters of the dictionary or list of movies and the length that the user typed in:
    #Dictionary for the movies that qualify the filter requirements.
    #for loop that loops through the lengths in the movie dictionary:
        #Check if that value matches the genre that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements

#Function that uses all of the helper function filters that has the parameters of the dictionary of movies and the requirements :
    #

#Function that acts as the main menu:
