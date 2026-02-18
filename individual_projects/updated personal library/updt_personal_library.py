#VY 2nd Personal Library
#import csv here
import csv

#list called books to save books with placeholder book
books = [
    {"Title": "Never Quit", "Author": "Jimmy Settle", "Year": "2018", "Genre": "Biography"},
]

#function for first saving CSV:
def save_csv():
    #try the following:
    try:
        #open the provided movies list and set the mode to "r" for reading as sample:
        with open("individual_projects/new_personal_library.csv", mode= "r") as sample:
            #read sample and set it to the variable read_list
            read_list = csv.reader(sample)
            #make a variable that grabs the next value in the CSV reader
            next_item = next(read_list)
            #make an empty list called "library"
            library = []
            #Use a for loop here to make a dictionary:
            for line in read_list:
                library.append(
                    {
                        next_item[0]: line[0],
                        next_item[1]: line[1],
                        next_item[2]: line[2],
                        next_item[3]: line[3]
                    }
                )
                #append the dictionary with the respective information (found using index values)
    #except statement here if the try doesn't work:
    except:
        print("The CSV doesn't exist.")
        #show that the CSV doesn't exist.
        #Return None
        return None
    #else statement:
    else:
        #Return library
        return library

#function for saving the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv():
    with open("individual_projects/new_personal_library.csv", "w", newline='') as csvfile:
        fieldnames = ['Title', 'Author', 'Year', 'Genre']
        writer = csv.DictWriter(csvfile, fieldnames)   #read through dictionary and write each row as a new thing in the CSV
        writer.writeheader()
        writer.writerows(books)

#Function named view_library for viewing the library with all details with parameters of library
def view_all_details(library):
    if library:
        print("Here is what currently is in your library:\n")
        #for loop here:
            #loop through the dictionary:
                #print out each book:
        for book in library:
            for item in book:
                #print out each movie
                print(f"{item}: {book[item]}")
                if item == "Author":
                    print("")   #space between each movie
    else:  #show this message if nothing is in the library
        print("There is nothing in your library.")

def view_simple_details(library):
    if library:
        print("Here is what currently is in your library:\n")
        #for loop here:
            #loop through the dictionary:
                #print out each book:
        for book in library:
            for item in book:
                if item == "Year":  #skip year and genre
                    print("")
                else:   #print only title and author
                    print(f"{item}: {book[item]}")

#function that uses the above two helper functions to allow the user to choose between the two ways of viewing.
def view_library():
    while True:
        view_how = print("Do you want to show only simple details(title and author only) or all details?(simple/all): ")
        if view_how.lower().strip() == "simple":
            view_simple_details(books)
            break
        elif view_how.lower().strip() == "all":
            view_all_details(books)
            break
        else:
            print("That isn't an option, please try again.")


#Function named add_item for adding a book to the library
def add_item():
    add_title = input("Title of the book you want to add: ")
    add_author = input("Author's full name: ")
    while True:  #stupidproofing for publishing year date
        add_year = input("Year of book's publishing: ")
        if not add_year.isnumeric():
            print("That isn't a year. Please try again.")
        else:
            break
    add_genre = input("Main genre of book: ")
    #add a new dictionary inside the books list for the new book.
    books.append({"Title": add_title.title().strip(), "Author": add_author.title().strip(), "Year": add_year.strip(), "Genre": add_genre.title().strip()})
    print(f"{add_title} by {add_author} was added to the library.")

#Function named remove_item for removing a book from the library (uses the get_input helper function)
def remove_item():
    while True:
        print("Please type the full title.")
        remove_title = input('\nTitle of book you want to remove: ').title()
        found_book = False
        #find the book that the user wants to find
        for info in books:
            if info["Title"] == remove_title:
                found_book = True
                #remove the info dictionary for the book that the user wants to remove. 
                print(f"{info['Title']} by {info['Author']} has been removed from the library.")
                books.remove(info)
                break
        if found_book:
            break
        else:  #make the user try again if they put in a book that didn't exist.
            print("That book doesn't exist. Please try again.")


#Function named search_item for searching for a book in the library
def search_item():
    #while True loop for stupid-proofing
    while True:
        print("What would you like to search by?: \n1. Title \n2. Author")
        search_by = input().title()

        if search_by == "1":
            added_books = {"Placeholder"}
            find_title = input("What's the title?: ")
            for info in books: #loop through the book list and get the dictionary for each book('s information)
                exist_book = info["Title"] + " by " + info["Author"]
                if find_title == info["Title"] and exist_book not in added_books:  #if it does exist and is not in added_books, add it to added_books
                    added_books.add(exist_book)
            added_books.remove("Placeholder")
            if added_books:
                print("\nHere are the books that came up:")  #show the books in a pretty format.
                for book in added_books:
                    print(book)
            else:
                print("Sorry, that book doesn't exist in this library.")
            break

        elif search_by == "2":
            added_books = {"Placeholder"}
            find_author = input("What's the author's full name?: ")
            for info in books:   #get the dictionary for each book's info
                exist_book = info["Title"] + " by " + info["Author"]
                if find_author == info["Author"] and exist_book not in added_books:
                    added_books.add(exist_book)
            added_books.remove("Placeholder")  #remove "Placeholder" so it won't be in the set.
            if added_books:
                print("Here are the books that came up:")  #show the books in a pretty format.
                for book in added_books:
                    print(book)
            else:
                print("Sorry, no authors by that name were found in this library.")
            break

        else:  #stupid-proofing
            print("That isn't an option. Please try again.")

#function to update a specific item
def update_item():
    while True:
        print("Please type the full title.")  #get user title
        update_title = input('\nTitle of book you want to update info for: ').title()
        found_book = False
        #find the book that the user wants to find
        for info in books:
            if info["Title"] == update_title:
                found_book = True
                old_title = info["Title"]  #save old title for sake of printing
                old_author = info["Author"]   #save old author for sake of printing
                info["Title"] = input("New title of book?: ").title().strip()
                info["Author"] = input("New author of book?: ").title().strip()
                while True: #stupid proofing for year number
                    info["Year"] = input("New year of book?: ").strip()
                    if not info["Year"].isnumeric():
                        print("That isn't a number. Please try again")
                    else:
                        break
                info["Genre"] = input("New genre of book?: ").title().strip()
                #remove the info dictionary for the book that the user wants to remove. 
                print(f"{old_title} by {old_author} has been updated to have this information: \n\tTitle: {info["Title"]} \n\tAuthor: {info["Author"]} \n\tPublishing Year: {info["Year"]} \n\tGenre: {info["Genre"]}")
                break
        if found_book:
            break
        else:  #stupid proofing
            print("That book doesn't exist. Please try again.")

#Function named main_menu for the main menu (this uses all other functions)
def main_menu():
    while True:
        print("\nType the number corresponding to the action you want to do:")
        print("\t1. View \n\t2. Add \n\t3. Remove \n\t4. Search \n\t5.Update a book's info \n\t6. Exit")
        user_action = input("Type what you want to do: ")
        if user_action == "1":
            view_library()
        elif user_action == "2":
            add_item()
            rewrite_csv()
        elif user_action == "3":
            remove_item()
            rewrite_csv()
        elif user_action == "4":
            search_item()
        elif user_action == "5":
            update_item()
        elif user_action == "6":
            break
        else:
            print("That isn't an option. Please try again.")

print("This is your personal library to keep track and store books.")

print("You can either view your library, add a book, remove a book, search for a book, or exit.")
print('When using this library, make sure you are using proper capitalization and spaces. \n(For example, instead of "never quit", type "Never Quit")\n')

books = save_csv()

view_all_details()
main_menu()

print("Goodbye.")