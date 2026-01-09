#VY 2nd Financial Calculator
import math #import math here

#Function for finding what type of calculator the user wants to use
def choose_function():
    #show what calculators are available
    print("Here are the calculators that you can choose from: \n1. Savings Time Calculator \n2. Compound Interest Calculator \n3. Budget Allocator \n4. Sales Price Calculator \n5. Tip Calculator")
    while True:
        #ask them what financial calculation they want. Set this value to a variable.
        calc_choice = input("Select an option: ")
        #Check what financial calculation they chose.
        #If it's not an option, force them to choose again.
        if not calc_choice.isnumeric or int(calc_choice) > 5:
            print("That is not an available option.")
        #If it is an option, return that option as the value for the function.
        else:
            break
    return calc_choice

#make a function that gets the original money. Like, asking the user what amount they're saving to, their starting amount, etc based on the calculator. This acts as a stupid-proof and removing redundancy thing.
def get_money(user_calc):
    #Make a variable set to 0 called "user_money". This is a placeholder name meant to be vague as it's whole point is to get the user input.
    user_money = 0
    while True:
        #If it's savings time calculator, ask what amount they are saving to.
        if user_calc == "1":
            user_money = input("What amount are you saving to?: ")
        #If it's compound interest, ask their starting amount.
        elif user_calc == "2":
            user_money = input("What is your starting amount?: ")
        #If it's budget allocator, ask their monthly income.
        elif user_calc == "3":
            user_money = input("What is your monthly income?: ")
        #If it's sales price, ask the original cost of the item.
        elif user_calc == "4":
            user_money = input("What is the original cost of the item?: ")
        #If it's tip calculator, ask for the value of the bill.
        elif user_calc == "5":
            user_money = input("What is the cost of the bill?: ")

        #If the user input is not a number, tell them to input again.
        elif not user_money.isnumeric():
            print("That is not a number, please try again.")
        #If it is, convert it into a float (2 digits).
        else:
            user_money = float(user_money)
            break
    #Return "user_money"
    return user_money


#Make one function for the Savings time Calculator with a parameter of goal_money
def savings_time(goal_money):
    print("Savings Time Calculator:")
    #Ask how often they are contributing (set this via numbers, such as 1 corresponds to weekly and 2 corresponds to monthly. Tell the user this/show the options to the user.)
    contri_time = input("How often are you contributing?(1. Weekly, 2. Monthly): ")
    if contri_time == "1":
        contri_time = "weeks"
    elif contri_time == "2":
        contri_time = "months"
    #Ask them how much they are contributing each time.
    contri_val = int(input("How much are you contributing each time?: "))

    #Divide the goal amount by how much they are contributing each time.
    total_time = goal_money/contri_val
    #Show how long it will take (with either weeks or months) to save the amount they want to reach to.
    print(f"It will take {total_time} {contri_time} to save ${goal_money:.2f}.")

#Compound interest calculator function with parameter of starting amount
def compound_interest(start_amount):
    #ask for their interest rate percent as a whole number/integer
    interest_rate = input("What is your interest rate percentage?(as an integer): ")
    #Ask their years spent compounding
    #yeah figure this out later figure out how to calculate this
    #Print out the money they will have after the time the user typed in.

#Budget Allocator calculator with a parameter of monthly income
    #Ask how many budget categories they have
    #Let them type in as many categories as they say they have. (the names). 
    #Go through and ask what percent (as an integer) they spend on each cateogry (use a loop. This part will most likely be the inner function)
    #Using the percentages and their monthly income, print out each category and how much they spend on each.

#Sales Price calculator with a parameter of original cost
    #Ask the discount as a percentage
    #Subtract the discount from 100. Then use this number as the percentage and multiply it by the original cost to get the discounted price.
    #Print out how much the item costs with the discount.

#Tip calculator with a parameter of bill
    #Ask them how much is the tip as a percentage.
    #Divide this number by 100 and then multiply this number by the bill. However, set this new value to a new variable.
    #Finally, add the original bill to the tip.
    #Print out the tip amount and the total.


#Greet the user and start a while Loop (so the user can do as many calculations as they want)
while True:
    #Run the function for finding what calculator the user wants to use.
    user_choice = choose_function()
    #Run the function for the calculator that the user chose.
    #Ask the user if they want to do another calculation
    #If the user wants to leave, say goodbye and break out of the while loop
    #If not, do another loop.