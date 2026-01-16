#VY 2nd Personal Library

#Create a list with two books in it to display for the user as an example. Name this "existing_books".
existing_books = ["Never Quit", "20,000 Leagues Under the Sea"]
#Create a list with two authors (corresponding to the books) to display for the user as an example. Name this "existing_authors".
existing_authors = ["Jimmy Settle", "Jules Verne"]
#These two lists should be the exact same length at all times and the index numbers should match so the book and author match.et

#Function named view_library for viewing the library
def view_library():
    #Use a for loop to loop through the list, existing_books, and use the index number to print the authors out as well.. Put each one on a new line for good formatting.
    print("Here is what currently is in your library:\n")
    for book in range(len(existing_books)):
        print(f"{existing_books[book]} by {existing_authors[book]}")

#Function named add_item for adding a book to the library
def add_item():
    #Ask the user what book they want to add by title.
    add_title = input('Title of the book you want to add: ')
    #Ask the user who wrote the book (the author).
    add_author = input("Author's full name: ")
    #Add the book to existing_books and add the author to the existing_authors
    existing_books.append(add_title)
    existing_authors.append(add_author)
    print(f"{add_title} by {add_author} was added to the library.")

#Function named remove_item for removing a book from the library
def remove_item():
    #Print out the entire list by using a for loop (just like the view_library function, maybe just use the view_library function)
    view_library()
    while True:
        #Ask the user what the title of the book is that they want to remove.
        remove_title = input('\nTitle of book you want to remove: ')

        #Check if that title exists in existing_books
        if not remove_title in existing_books:
            #If it doesn't, ask them to select another one.
            print("That book doesn't exist. Please try again.")
        else:
            break
    #If it does, find the index of that book and remove it. Use the index number to remove the corresponding author.
    remove_index = existing_books.index(remove_title)
    print(f"{existing_books[remove_index]} by {existing_authors[remove_index]} has been removed from the library.")
    existing_books.pop(remove_index)
    existing_authors.pop(remove_index)

#Function named search_item for searching for a book in the library
def search_item():
    #Make a tuple named search_results for the search results.
    search_results = []
    while True:
        #Ask the user what they want to search by. Before giving them the option to input, tell them they can either search by title(1) or author(2)
        print("What would you like to search by?: \n1. Title \n2. Author")
        search_by = input()

        #If the user wants to search by title
        if search_by == "1":
            added_books = {"Placeholder"}
            #Ask them what the title is.
            find_title = input("What's the title?: ")
            #Check if the title exists in existing_books.
            for found in range(len(existing_books)):
                #concatenate the title and the author in the format "[book name] by [author]" and set it to variable "exist_book"
                exist_book = existing_books[found] + " by " + existing_authors[found]
                if find_title == existing_books[found] and exist_book not in added_books:
                    #If it is, add exist_book to the search results
                    added_books.add(exist_book)
            added_books.remove("Placeholder")
            if added_books:
                #Loop through search_results to print it out nicely by printing it out one by one.
                print("\nHere are the books that came up:")
                for book in added_books:
                    print(book)
            #If it doesn't exist, show that no results were found
            else:
                print("Sorry, that book doesn't exist in this library.")
            break

        #Do the same thing for authors.
        elif search_by == "2":
            added_books = {"Placeholder"}
            #Ask the author name
            find_author = input("What's the author's full name?: ")
            #find if it exists
            for found in range(len(existing_authors)):
                #concatenate the title and the author in the format "[book name] by [author]" and set it to variable "exist_book"
                exist_book = existing_books[found] + " by " + existing_authors[found]
                if find_author == existing_authors[found] and exist_book not in added_books:
                    #If it is, add exist_book to the search results
                    added_books.add(exist_book)
            added_books.remove("Placeholder")
            if added_books:
                #Loop through search_results to print it out nicely by printing it out one by one.
                print("Here are the books that came up:")
                for book in added_books:
                    print(book)
            #If it doesn't exist, show that no results were found
            else:
                print("Sorry, no authors by that name were found in this library.")
            break

        #Do stupidproofing
        else:
            print("That isn't an option. Please try again.")

#Function named main_menu for the main menu (this uses all other functions)
def main_menu():
    #While loop here so the user only leaves when they choose to
    while True:
        #Tell the user to type the number for the action they want to perform.
        print("\nType the number corresponding to the action you want to do.")
        #Show all the options and explain what they do (View is 1, Add is 2, Remove is 3, Search is 4, Exit is 5)
        print("1. View \n2. Add \n3. Remove \n4. Search \n5. Exit(This option will reset the library)")
        user_action = input("Type what you want to do: ")
        #If they chose 1, run view_library
        if user_action == "1":
            view_library()
        #If they chose 2, run add_item
        elif user_action == "2":
            add_item()
        #If they chose 3, run remove_item
        elif user_action == "3":
            remove_item()
        #If they chose 4, run search_item
        elif user_action == "4":
            search_item()
        #If they chose 5, break out of the while loop so the function will end.
        elif user_action == "5":
            break

#Greet the User and tell them that this is a peresonal library for books
print("This is your personal library to keep track and store books.")
#Explain what it is and how to use this personal library
print("You can either view your library, add a book, remove a book, search for a book, or exit. (Exiting this program will erase all data.)")
print('When using this library, make sure you are using proper capitalization and spaces. \n(For example, instead of "never quit", type "Never Quit")\n')
#Print out existing_books and existing_authors
view_library()

#Run main_menu
main_menu()
#Thank the user and say goodbye (this should only show when the user chooses to end the function)
print("Goodbye.")