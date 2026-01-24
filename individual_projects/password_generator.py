#VY 2nd Password Generator
#Import random here
import random

#Make a function named get_requirements that gets the password requirements that the user wants:
def get_requirements():
    user_responses = []
    requirements = ["How long do you want your passwords to be?(as an integer): ", "Does your password need uppercase letters?(y/n): ", "Does your password need lowercase letters?(y/n): ", "Does your password need numbers?(y/n): ", "Does your password need special characters?(y/n): "]
    for requirement in requirements:
        while True:
            print(requirement)
            response = input()
            if response.isnumeric() and "integer" in requirement:
                user_responses.append(response)
                break
            elif "y/n" in requirement:
                user_responses.append(response)
                break
            else:
                print("That's not an option. Please try again.")

    #Ask the user the password length they want(as an integer). save this input in a variable. Same goes for the rest of the inputs for the user.
    #ask_length = input("How long do you want your passwords to be?(as an integer): ")
    #Ask the user if the password needs uppercase letters(yes or no option)
    #ask_upper = input("Does your password need uppercase letters?(y/n): ")
    #Ask the user if the password needs lowecase letters (yes or no)
    #ask_lower = input("Does your password need lowercase letters?(y/n): ")
    #Ask the user if the password needs numbers (yes or no)
    #ask_number = input("Does your password need numbers?(y/n): ")
    #Ask the user if the password needs special characters (yes or no)
    #ask_special = input("Does your password need special characters?(y/n): ")

    #Return all these values.
    return user_responses[0], user_responses[1], user_responses[2], user_responses[3], user_responses[4]


#Make a function named get_characters that compiles the requirement for the passwords. It needs the parameters that check if a certain requirement is needed, such as if the password needs uppercase letters or not. This does not include the length
def get_characters(upper_requir, lower_requir, number_requir, special_requir):
    #Make an empty list for the available characters in ASCII code, named available_characters.
    available_characters = []

    #If the user wants uppercase letters:
    if upper_requir.lower().strip() == "y":
        #Add ASCII codes 65 to 90 (A-Z)
        available_characters.extend(range(65, 91))
    #If the user wants lowercase letters:
    if lower_requir.lower().strip() == "y":
        #Add ASCII codes 97 to 122 (a-z)
        available_characters.extend(range(97, 123))
    #If the user wants numbers:
    if number_requir.lower().strip() == "y":
        #Add ASCII codes 48 to 57 (0-9)
        available_characters.extend(range(48, 58))
    #If the user wants special characters:
    if special_requir.lower().strip() == "y":
        #Add common special character ranges: 33-47, 58-64, 91-96, 123-126
        available_characters.extend(range(33, 48))
        available_characters.extend(range(58, 65))
        available_characters.extend(range(91, 97))
        available_characters.extend(range(123, 127))

    #Return available_characters
    return available_characters


#Make a function named save_passwords that gets the passwords and stores them in preparation of printing them out to the user. It needs a parameter that has characters in ASCII code as well as the parameter of how long a password should be:
def save_passwords(character_codes, password_length):
    #Make an empty list for the four passwords to store them, named new_passwords.
    new_passwords = []
    #Make an inner function named make_password that actually makes passwords:
    def make_password():
        #An empty string named new_password. This is so the program can actually build the password and then it can be appended to the list.
        new_password = ""
        #A for loop here that loops as many times as how long the user wants their passwords to be:
        for i in range(int(password_length)):
            #From the list of ASCII codes, randomly pick one out by using the random module. Set this to variable new_code
            new_code = random.choice(character_codes)
            #Turn new_code into a character and set it to variable new_character
            new_character = chr(new_code)
            #Add new_character to new_password.
            new_password += new_character
        #Return new_password
        return new_password

    #Make a for loop here that loops 4 times:
    for i in range(4):
        #Add make_password to new_passwords
        new_passwords.append(make_password())
    #Return new_passwords
    return new_passwords

#Make a function named main_menu:
def main_menu():
    while True:
        #Ask the user what they want to do
        print("\nYou can: \n1. Generate Codes \n2. Exit")
        user_action = input("What would you like to do?: ")
        if user_action == "1":
            #Run get_requirements and set each returned value to a new variable(variables length_check, upper_check, lower_check, number_check, special_check).
            length_check, upper_check, lower_check, number_check, special_check = get_requirements()
            #Run get_characters with parameters upper_check, lower_check, number_check, and special_check, and set this to useable_characters
            useable_characters = get_characters(upper_check, lower_check, number_check, special_check)
            #Run save_passwords with parameters useable_characters and length_check, and save it to final_passwords.
            final_passwords = save_passwords(useable_characters, length_check)
            #Use a for loop to properly print out final_passwords in a formatted and clean way.
            print("Here are your generated passwords:")
            counter = 1              #counter for using as a number to list out passwords
            for password in final_passwords:
                print(f"{counter}. {password}")
                counter += 1
        elif user_action == "2":
            break
        else:
            print("That's not an option. Please try again.")

#Greet the user and explain to them that this is a password generator and how it works.
print("This is a password generator.")
main_menu()

#Thank the user and say goodbye.
print("Thanks for using this password generator.")