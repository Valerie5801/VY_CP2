#VY 2nd Menu for Word Counter
#import menu_actions
import menu_actions
import time_clean_functions
import helper_functions_read

#main_menu function:
def main_menu(document_info, document_content):
    #while True loop here:
    while True:
        #show the title "Document word count updater"
        print("---Document Word Count Updater---")
        #show the user what they can do: 1. Update document info (gets new file path), 2. View document, 3. Add content to document, 4. Exit the program
        print("You can: \n\t1. Update Document File Path  \n\t2. View Document \n\t3. Add Content To Document  \n\t4. Rewrite Document \n\t5. Show details \n\t6. Exit")
        #Ask the user for what they want to do
        user_action = input("What do you want to do?: ")
        match user_action:
            #If they chose option 1:
            case "1":
                #run the function that updates the file path (from menu_actions)
                document_info = menu_actions.update_path(document_info)
                time_clean_functions.edit_info(document_info)
            #If they chose option 2:
            case "2":
                #run the function that shows the txt file document (from menu_actions)
                menu_actions.show_doc()
            #If they chose option 3:
            case "3":
                #run the function that lets the user add content (from menu_actions)
                new_content = menu_actions.add_content(document_content)
                helper_functions_read.add_doc(new_content)
            case "4":
                
            #If they chose option 6:
            case "6":
                #break out of the while loop
                break
            case _:
            #Stupid proof here in case the user typed in something invalid.
                print("That is not an option. Please try again.")
        # Update CSV with current word count and timestamp before saving
        document_info[0]["Word Count"] = str(helper_functions_read.get_word_count(document_content))
        document_info[0]["Last Edited"] = str(helper_functions_read.get_time())
        time_clean_functions.edit_info(document_info)
        document_content = helper_functions_read.save_doc()