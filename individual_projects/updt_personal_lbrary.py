#VY 2nd Personal Library
#import csv here
import csv

#empty dictionary called books to save books with placeholder books
books = [
    {"Title": "Never Quit", "Author": "Jimmy Settle"},
    {"Title": "20,000 Leagues Under the Sea", "Author": "Jules Verne"}
]

#function for first saving CSV:
def first_save_csv():
    #try the following:
    try:
        #open the provided movies list and set the mode to "r" for reading as sample:
        with open("individual_projects\new_personal_library.csv", mode= "r") as sample:
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

#function for saving the CSV again:
def rewrite_csv():
    with open("notes/test.csv", "r+", newline='') as csvfile:
        fieldnames = ['Title', 'Author']
        reader = csv.reader(csvfile)
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writerows(books)

#Function named view_library for viewing the library with parameters of library
def view_library(library):
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


#Function named add_item for adding a book to the library
def add_item():
    add_title = input('Title of the book you want to add: ')
    add_author = input("Author's full name: ")
    existing_books.append(add_title)
    existing_authors.append(add_author)
    print(f"{add_title} by {add_author} was added to the library.")

#Function named remove_item for removing a book from the library
def remove_item():
    while True:
        remove_title = input('\nTitle of book you want to remove: ')

        if not remove_title in existing_books:
            print("That book doesn't exist. Please try again.")
        else:
            break
    remove_index = existing_books.index(remove_title)
    print(f"{existing_books[remove_index]} by {existing_authors[remove_index]} has been removed from the library.")
    existing_books.pop(remove_index)
    existing_authors.pop(remove_index)

#Function named search_item for searching for a book in the library
def search_item():
    search_results = []
    while True:
        print("What would you like to search by?: \n1. Title \n2. Author")
        search_by = input()

        if search_by == "1":
            added_books = {"Placeholder"}
            find_title = input("What's the title?: ")
            for found in range(len(existing_books)):
                exist_book = existing_books[found] + " by " + existing_authors[found]
                if find_title == existing_books[found] and exist_book not in added_books:
                    added_books.add(exist_book)
            added_books.remove("Placeholder")
            if added_books:
                print("\nHere are the books that came up:")
                for book in added_books:
                    print(book)
            else:
                print("Sorry, that book doesn't exist in this library.")
            break

        elif search_by == "2":
            added_books = {"Placeholder"}
            find_author = input("What's the author's full name?: ")
            for found in range(len(existing_authors)):
                exist_book = existing_books[found] + " by " + existing_authors[found]
                if find_author == existing_authors[found] and exist_book not in added_books:
                    added_books.add(exist_book)
            added_books.remove("Placeholder")
            if added_books:
                print("Here are the books that came up:")
                for book in added_books:
                    print(book)
            else:
                print("Sorry, no authors by that name were found in this library.")
            break

        else:
            print("That isn't an option. Please try again.")

#Function named main_menu for the main menu (this uses all other functions)
def main_menu():
    while True:
        print("\nType the number corresponding to the action you want to do.")
        print("1. View \n2. Add \n3. Remove \n4. Search \n5. Exit(This option will reset the library)")
        user_action = input("Type what you want to do: ")
        if user_action == "1":
            view_library()
        elif user_action == "2":
            add_item()
        elif user_action == "3":
            remove_item()
        elif user_action == "4":
            search_item()
        elif user_action == "5":
            break

print("This is your personal library to keep track and store books.")

print("You can either view your library, add a book, remove a book, search for a book, or exit. (Exiting this program will erase all data.)")
print('When using this library, make sure you are using proper capitalization and spaces. \n(For example, instead of "never quit", type "Never Quit")\n')

view_library()
main_menu()

print("Goodbye.")