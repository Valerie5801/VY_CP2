#VY 2nd Simple Morse Code Translator

#Make two tuples
#One for the alphabet in English
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
#One for the alphabet in Morse Code
morse_alpha = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")
morse_chars = {".", "-"}

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
        if user_message.isalpha():
            break
        else:
            for char in user_message:
                if char not in morse_chars:
                    full_morse = False
            if full_morse:
                break
            else:
                print("Your message isn't in full morse code or fully alphabetical. Please try again.")
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
    #split the coded message and set the reuslting list to split_coded
    split_coded = coded_message.split()
    #Make a for loop that loops through split_coded:
    for char in range(len(split_coded)):
        #check if the character is a /. If so, append a space to coded_message
        if char == "/":
            decoded_message.append(" ")
        #Check if each value matches one from the alphabet list
        #if it does, get the index of the matched value:
        elif split_coded[char] == alphabet[char]:
            #use that index to find the corresponding coded letter and add it to decoded_message.
            decoded_message += alphabet[char]
        #if not, move on.
    #return decoded_message
    return decoded_message

#Make a function to translate English into Morse Code with a parameter of the message that needs to be translated:
def english_morse(decoded_message):
    #Make an empty string named coded_message
    coded_message = ""
    #Split the message and set the resulting list to split_message
    split_message = decoded_message.split()
    #Make a for loop that loops through split_message:
    for char in range(len(decoded_message)):
        #check if each value matches one from the morse code list.
        #if it does, get the index of the matched value:
        if split_message[char] == alphabet[char]:
            #use that index to find the corresponding coded letter and add that to coded_message.
            coded_message +=
        #if not, move on.
    #return coded_message


#Make a function named main_menu:
    #While true loop here.
        #Make an empty string named user_input
        #Ask the user if they want to translate from morse code to english, english to morse code, or exit.
        #If the user wants to translate morse code to english:
            #Run the function to get inputs from the user and set it to user_input
            #run the function to translate morse code into english using user_input as parameters.
        #if the user wants to translate english to morse code:
            #run the function to get inputs form the user and set it to user_input
            #Run the function to translate morse code into english using user_input as parameters.
        #If the user wants to exit:
            #break out of the while loop
        #Stupid proof here incase the user types in something that isn't valid.

#Greet the user and explain that this is a morse code translator. also let them know that numbers in numerical form (such as 1 and 2) are not accommodated and other disclaimers.
#Run the main_menu function
#Thank the user for using the morse code translator.