#VY 2nd Main Menu for Simple Gradebook
import csv
import action_funcs as act
from classes import GradeBook
import helper

def user_menu():
    #count the amount of students and show it to the user
    #show the user what they can do:
        #1. Add new student
        #2. Add a grade to a specific student
        #3. Remove a student
        #4. View a Student's record
        #5. Edit a student
        #6. View all students/Gradebook
        #7. Exit
    gradebook = GradeBook()

    while True:
        #ask the user what they want to do. run the corresponding function from action_funcs, and sanitize for invalid inputs
        print("You can: \n\t1. Add new student\n\t2. Add a grade to a student\n\t3. Remove a student\n\t4. View a student's record\n\t5. Edit a student\n\t6. View all students/gradebook\n\t7. Exit")
        print('Please type in numerical input such as 1 for "Add new student"')
        user_action = input("What do you want to do?: ")
        
        match user_action:
            case "1":
                act.add_student()
            case "2":
                #ask the user what the id is of that student
                print("What is the ID of the student you want to remove?")
                find_id = int(helper.check_num())
                #check if the id exists
                #if it doesnt:
                    #say that the student doesn't exist
                    #end the function
                #if it does exist:
                    #run the add_grade function
                act.add_grade()
            case "3":
                act.remove_student()
            case "4":
                act.student_record()
            case "5":
                act.edit_student()
            case "6":
                #use the show_students method from the GradeBook class
                gradebook.show_students()
            case "7":
                break
            case _:
                print("That isn't an option. Please type a numerical input to select your action.")
