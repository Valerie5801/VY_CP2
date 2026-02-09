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
def get_filters():
    #Print the available filters to apply (and let them know it has to be separated with commas with no spaces.)
    print("You can filter by: \n1. Genre \n2. Directors \n3. Important Actor \n4. Length")
    #Genre is 1, Director is 2, Actor is 3, Length is 4.
    while True:
        #Ask the user what filters they want to apply (via corresponding numbers).
        ask_filters = input("What filters do you want to apply?(separate them with commas like this: 1,2,4): ")
        #Stupid proof here incase the user doesn't type something that is recognizeable by the program.
        if not "1" in ask_filters or not "2" in ask_filters or not "3" in ask_filters or not "4" in ask_filters:
            print("Please use numbers and commas.")
        else:
            break

    #Return the filters that the user wants to apply
    return ask_filters

#Function that gets user input with parameter of the filters that the user wants (as numbers 1-4):
def specific_filters(user_filters = "1,2,3,4"):
    #Make a list named "requirements". This will be used as the list for the filters that should be applied when searching for movies.
    requirements = []
    #If 1 is in the string of filters that the user wants:
    if "1" in user_filters:
        #Ask the user for the genre they want and provide an example of how it should be formatted.
        ask_genre = input("What genre do you want to apply?: ").strip().title()
        #Append this to requirements
        requirements.append(ask_genre)
    #If 2 is in the string of filters that the user wants:
    if "2" in user_filters:
        #Ask the user of the name of the director, at least the first name.
        ask_director = input("What is the name of the director you are looking for?(you can provide only the first name or the full name): ").title().strip()
        #Append this to requirements
        requirements.append(ask_director)
    #If 3 is in the string of filters that the user wants:
    if "3" in user_filters:
        #Ask for one name of an actor they want to find movies about.
        ask_actor = input("What is the name of an actor you are looking for?(you can provide only the first name or the full name): ").title().strip()
        #Append this to requirements.
        requirements.append(ask_actor)
    #If 4 is in the string of filters that the user wants:
    if "4" in user_filters:
        #Ask the for the length of the movie in minutes
        while True:
            ask_length = input("What's the length that you are looking for?(in minutes): ")
            if not ask_length.isnumeric():
                print("Please give your answer as an integer.")
            else:
                requirements.append(int(ask_length))
                break
        #Return requirements
    return requirements

#Helper function that filters by genre and has parameters of the dictionary or list of movies and the name of the genre that the user typed in:
def filter_genre(movie_list, genre_name = ""):
    #Dictionary for the movies that qualify the filter requirements.
    meets_require = []
    #for loop that loops through the genres in the movie list:
    for movie in movie_list:
        for genre in movie:
            if movie["Genre"] == genre_name:
                meets_require.append(movie)
            #Check if that value matches the genre that the user chose.
            #If it does:
                #Add it to the dictionary
    #Return the dictionary for movies that met the requirements
    return meets_require

#Helper function that filters by directors and has parameters of the dictionary or list of movies and the name of the director that the user typed in:
def filter_directors(movie_list, director_name = ""):
    #Dictionary for the movies that qualify the filter requirements.
    meets_require = []
    #for loop that loops through the directors in the movie dictionary:
    for movie in movie_list:
        for director in movie:
            if movie["Director"] == director_name:
                meets_require.append(movie)
        #Check if that value matches the director that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements
    return meets_require

#Helper function that filters by important actors and has parameters of the dictionary or list of movies and the name of the important actor(s) that the user typed in:
def filter_actors(movie_list, actor_name = ""):
    #Dictionary for the movies that qualify the filter requirements.
    meets_require = []
    #for loop that loops through the important actors in the movie dictionary:
    for movie in movie_list:
        for actor in movie:
            if movie["Notable Actors"] == actor_name:
                meets_require.append(movie)
        #Check if that value matches the genre that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements
    return meets_require

#Helper function that filters by length and has parameters of the dictionary or list of movies and the length that the user typed in:
def filter_length(movie_list, length = 0):
    #Dictionary for the movies that qualify the filter requirements.
    meets_require = []
    #for loop that loops through the lengths in the movie dictionary:
    for movie in movie_list:
        for length in movie:
            if movie["Length"] == length:
                meets_require.append(movie)
        #Check if that value matches the genre that the user chose.
        #If it does:
            #Add it to the dictionary
    #Return the dictionary for movies that met the requirements
    return meets_require

#Function that uses all of the helper function filters that has the parameters of the dictionary of movies and the requirements:
    #

#Function that acts as the main menu:
