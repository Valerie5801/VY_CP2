#VY 2nd Simple Morse Code Translator

#Make two tuples
#One for the alphabet in English
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#One for the alphabet in Morse Code
morse_alpha = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
morse_chars = {".", "-", "/", " "}
options = ["1", "2", "3"]

#Make a function to get the inputs from the user:
def get_input(user_choice = "2"):
    #boolean flag to check if a message is fully morse code
    full_morse = True
    #While loop here.
    while True:
        #Ask the user what message they would like translated. Set this to user_message
        if user_choice == "1":
            print("Please put a space between each letter, and a / between each word with a space on each side of the /.")
        user_message = input("What message would you like translated?: ")
        #Check if the message either has dots and dashes or is alphabetical.
        check_message = user_message.split()
        for word in check_message:
            full_morse = True
            if word.isalpha() and user_choice == "2":
                continue
            elif user_choice == "1" and word.isalpha():
                    print("You are translating from morse code into english. Please try again.")
            else:
                for char in user_message:
                    if char not in morse_chars:
                        full_morse = False
                if full_morse:
                    continue
                else:
                    print("Your message isn't in morse code or in English. Please try again.")
                    break
        break
        #If it's not:
            #Ask the user to try again.
        #if it is:
            #break out of the while loop.
    user_message = user_message.lower()
    #return user_message
    return user_message

#Make a function to translate Morse Code into English with a parameter of the message that needs to be translated:
def morse_english(coded_message):
    #Make an empty string named decoded_message
    decoded_message = ""
    #split the coded message by / to separate words
    split_words = coded_message.split(" / ")
    #Make a for loop that loops through each word
    for word in split_words:
        #split each word by spaces to separate morse characters
        split_coded = word.split()
        #loop through each morse character
        for char in split_coded:
            #find the index of the morse character in morse_alpha
            if char in morse_alpha:
                index = morse_alpha.index(char)
                #add the corresponding english letter to decoded_message
                decoded_message += alphabet[index]
        decoded_message += " "
    #return decoded_message
    return decoded_message.strip()

#Make a function to translate English into Morse Code with a parameter of the message that needs to be translated:
def english_morse(decoded_message):
    #Make an empty string named coded_message
    coded_message = ""
    #Split the message to separate words
    split_message = decoded_message.split()
    #Make a for loop that loops through each word
    for word in split_message:
        #loop through each character in the word
        for char in word:
            #find the index of the character in alphabet
            if char in alphabet:
                index = alphabet.index(char)
                #add the corresponding morse code to coded_message
                coded_message += morse_alpha[index] + " "
        #add a / with spaces to separate words
        coded_message += "/ "
    #return coded_message
    return coded_message.strip(" /")


#Make a function named main_menu:
def main_menu():
    #While true loop here.
    while True:
        #Ask the user if they want to translate from morse code to english, english to morse code, or exit.
        print("\nYou can: \n1. Translate from Morse code to english \n2. Translate from english to morse code \n3. Exit")
        #Stupid proof here incase the user types in something that isn't valid.
        while True:
            user_choice = input("What do you want to do?(1/2/3): ")
            if user_choice not in options:
                print("That isn't an option, please try again.")
            else:
                break

        #Run the function to get inputs from the user and set it to user_input
        if user_choice == "1" or user_choice == "2":
            user_input = get_input(user_choice)
        match user_choice:
            #If the user wants to translate morse code to english:
            case "1":
                #Run the function to translate morse code into english using user_input as parameters.
                print(morse_english(user_input))
            #if the user wants to translate english to morse code:
            case "2":
                print(english_morse(user_input))
                #Run the function to translate morse code into english using user_input as parameters.
            #If the user wants to exit:
            case "3":
                #break out of the while loop
                break

#Greet the user and explain that this is a morse code translator. also let them know that numbers in numerical form (such as 1 and 2) are not accommodated and other disclaimers.
print("This is a morse code translator. You can translate from morse code into English and vice versa. \nThis translator doesn't accommodate for special symbols or numbers. Spaces between words in morse code is shown with a /")
#Run the main_menu function
main_menu()
#Thank the user for using the morse code translator.
print("Goodbye.")