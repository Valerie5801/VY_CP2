#VY 2nd Main for Word Counter
#import the menu function from the user_menu file
import user_menu
#import helper_functions_read
import helper_functions_read
import time_clean_functions

#make the list that holds the text document lines
doc_lines = helper_functions_read.save_doc()
#make a list that will hold the CSV data. This will start as empty through each run since it will have it's value set every time this is run to make sure its info is up to date.
csv_data = time_clean_functions.save_info()


#Greet the user and explain that this is a word counter and how it works
print("This is a word counter. You can look at your document, edit it, and see how many words are in it.")
#run the main_menu function
user_menu.main_menu(csv_data, doc_lines)
#Say goodbye to the user.
print("Thanks for using the word counter.")