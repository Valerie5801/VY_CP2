#VY 2nd Action Functions for Simple Gradebook
from .classes import Student
from . import helper
import time as t

#function to add a grade to an existing student
def add_grade(student):
    #ask the user how many grades they want to add with a max of six.
    print("\nYou can only add a max of 6 grades to each student.")
    print("How many grades do you want to add?(please type as a whole number)")
    #make sure the user types in a number between 0 and 6
    try:
        amount_grade = max(0, min(int(helper.check_num()), 6))
    except ValueError:
        print("Invalid input. Setting to 0 grades.")
        amount_grade = 0

    for i in range(amount_grade):
            print("\nType the percentage of the grade (don't type %)")
            try:
                user_added_grade = int(helper.check_num())
                student.add_grade(user_added_grade)
            except ValueError:
                print("Invalid grade. Skipping this grade.")
                continue

    return student


#function to add a student
def add_student():
    #ask the user the name of the student
    new_name = input("\nWhat is the name of the student?: ").strip().title()
    #ask the user for the student id (make sure it's a number by using the helper function that stupidproofs numbers)
    print("Please type the ID of the student as a number.")
    new_id = int(helper.check_num())
    #use the Student class (found from the classes.py file) with the information
    new_student = Student(new_name, new_id)

    #ask the user if they would like to add grades to the student
    while True:
        ask_add = input("Would you like to add a grade for this student?(type in y/n): ").lower().strip()
        match ask_add:
            case "y":
                #run add_grade
                new_student = add_grade(new_student)
                #break out of the loop
                break
            case "n":
                break
            case _:
                print('That is not an option. Please type either "y" or "n"')

    new_student.find_avg()
    new_student.letter_average()
    new_student.return_info()
    
    print(f"{new_student.name} has been added with the following information.")
    print(new_student)

    #return the student
    return new_student


#function to remove a student
def remove_student(gradebook, student):
    #use the .remove() method from the gradebook class
    print(f"\nRemoving {student.name}...")
    gradebook.student_list.remove(student)
    t.sleep(1)
    print(f"\n{student.name} has been removed.")


#function to view a student's record
def student_record(student):
    #use the __str__ method from Student class
    print("\n---Student Record---")
    print(student)


#function to edit a student
def edit_student(student):
    #while true loop
    while True:
        #show the student
        print(f"\nHere is the information about {student.name}.")
        print(student)
        #ask the user what they want to edit (name, student ID, grades) or if they want to exit
        print("\nYou can: \n\t1. Edit the Student's name\n\t2. Edit the Student's ID\n\t3. Edit their grades\n\t4. Exit")
        print("\nPlease type the number of the respective option.")
        print("What do you want to do?")
        user_action = int(helper.check_num())
        match user_action:
            #if they want to edit the name:
            case 1:
                #ask the user what the new name for the student will be
                new_name = input("What will the name of the student be?").title().strip()
                #set it to the student's name in the object
                student.name = new_name
            #elif they want to edit the student ID:
            case 2:
                #ask the user what the new student ID for the student will be
                print("What will the new ID be?")
                new_id = int(helper.check_num())
                #set it to the student's id in the object
                student.student_id = new_id
            #elif they want to edit the grades:
            case 3:
                #show the grades
                for i in range(len(student.grade_list)):
                    print(f"Grade {i+1}: {student.grade_list[i]}")
                #ask what grade they want to edit (it will be labeled Grade 1, Grade 2, Grade 3, etc...)
                print('What grade do you want to edit?(Type in the grade such as "1" for Grade 1): ')
                edited_grade = int(helper.check_num())
                edited_grade -= 1
                #if the grade doesn't exist, tell the user and continue with the loop
                #if the grade does exist:
                    #ask the user what the new grade will be
                    #set the new grade for the grade that the user selected
                if 0 <= edited_grade < len(student.grade_list):
                    print("If you want to remove the grade, type in 0 for its value.")
                    new_grade = int(helper.check_num())
                    student.grade_list[edited_grade] = new_grade
                elif len(student.grade_list) <= 6:
                    #if it is possible for the grade to exist but doesn't exist yet, make them make the new grade.
                    print("It looks like that grade doesn't exist yet. Let's make one.")
                    student = add_grade(student)
                else:
                    print("There is a max of 6 grades. Perhaps you typed in a word or a number higher than 6?")
            #elif they want to leave:
            case 4:
                break
                #break out of the while loop
            #else if they typed something in that wasn't valid:
            case _:
                #tell the user that it isn't an option
                print("That is not a valid option. Please type in the number corresponding to the option.")
    #return the student
    return student