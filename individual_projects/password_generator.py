#VY 2nd Password Generator
#Import random here
import random

#Make four lists, all with the ASCII values of each category. This is for easy access.
upper_codes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
lower_codes = [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
number_codes = []
special_codes = []

#Make a function named get_requirements that gets the password requirements that the user wants:
def get_requirements():
    #Ask the user the password length they want(as an integer). save this input in a variable. Same goes for the rest of the inputs for the user.
    ask_length = input("How long do you want your passwords to be?(as an integer): ")
    #Ask the user if the password needs uppercase letters(yes or no option)
    ask_upper = input("Does your password need uppercase letters?(y/n): ")
    #Ask the user if the password needs lowecase letters (yes or no)
    ask_lower = input("Does your password need lowercase letters?(y/n): ")
    #Ask the user if the password needs numbers (yes or no)
    ask_number = input("Does your password need numbers?(y/n): ")
    #Ask the user if the password needs special characters (yes or no)
    ask_special = input("Does your password need special characters?(y/n): ")

    #Return all these values.
    return ask_length, ask_upper, ask_lower, ask_number, ask_special


#Make a function named get_characters that compiles the requirement for the passwords. It needs the parameters that check if a certain requirement is needed, such as if the password needs uppercase letters or not. This does not include the length
def get_characters(upper_requir, lower_requir, number_requir, special_requir):
    #Make an empty list for the available characters in ASCII code, named available_characters.
    available_characters = []

    #If the user wants uppercase letters:
    if upper_requir == "y":
        #Add numbers 65 to 90 to available_characters
        for code in upper_codes:
            available_characters.append(code)
    #If the user wants lowercase letters:
    if lower_requir == "y":
        #Add numbers 97 to 122 to available_characters
        for code in lower_codes:
            available_characters.append(code)
    #If the user wants numbers:
    if number_requir == "y":
        #Add numbers 48 to 57 to available_characters
        for code in nu:
            available_characters.append(code)
    #If the user wants special characters:
        #Add numbers 33 to 47 to available_characters

    #Return available_characters


#Make a function named save_passwords that gets the passwords and stores them in preparation of printing them out to the user. It needs a parameter that has characters in ASCII code as well as the parameter of how long a password should be:
    #Make an empty list for the four passwords to store them, named new_passwords.
    #Make an inner function named make_password that actually makes passwords:
        #An empty string named new_password. This is so the program can actually build the password and then it can be appended to the list.
        #A for loop here that loops as many times as how long the user wants their passwords to be:
            #From the list of ASCII codes, randomly pick one out by using the random module. Set this to variable new_code
            #Turn new_code into a character and set it to variable new_character
            #Add new_character to new_password.
        #Return new_password

    #Make a for loop here that loops 4 times:
        #Add make_password to new_passwords
    #Return new_passwords

#Make a function named main_menu:
    #Run get_requirements and set each returned value to a new variable(variables length_check, upper_check, lower_check, number_check, special_check).
    #Run get_characters with parameters upper_check, lower_check, number_check, and special_check, and set this to useable_characters
    #Run save_passwords with parameters useable_characters and length_check, and save it to final_passwords.
    #Use a for loop to properly print out final_passwords in a formatted and clean way.

#Greet the user and explain to them that this is a password generator and how it works.
#While loop here:
    #Ask the user if they want to generate passwords or exit the program.
    #If the user wants to generate passwords:
        #Run main_menu
    #Elif the user wants to exit the program:
        #Break out of the while loop

#Thank the user and say goodbye.