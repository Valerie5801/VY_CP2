#VY 2nd Action Functions for Simple Gradebook
from classes import Student
import helper

#function to add a student
def add_student():
    #ask the user the name of the student
    new_name = input("What is the name of the student?: ")
    #ask the user for the student id (make sure it's a number by using the helper function that stupidproofs numbers)
    print("Please type the ID of the student as a number.")
    new_id = int(helper.check_num())
    #use the Student class (found from the classes.py file) with the information
    new_student = Student(new_name, new_id)

    #ask the user if they would like to add grades to the student
    while True:
        add_grade = input("Would you like to add a for this student?(type in y/n): ")
        match add_grade.lower().strip():
            case "y":
                #ask the user how many grades they want to add with a max of six.
                #break out of the loop.
                print("letting you add grades")
            case "n":
                break
            case _:
                print('That is not an option. Please type either "y" or "n"')

    #return the student
    return new_student


#function to add a grade to an existing student
def add_grade(student):
    #ask the user how many grades they want to add.
    print("How many grades do you want to add?")
    num_grades = int(helper.check_num())

    #as the student parameter should be an object, use the add_grade method from the Student clas
    for grade in num_grades:
        print(f"What is the grade of Grade {grade}?")
        ask_grade = helper.check_num()
        student.add_grade(ask_grade)

    return student


#function to remove a student
def remove_student(students):
    #ask the user what the id is of that student
    print("What is the ID of the student you want to remove?")
    find_id = int(helper.check_num())
    #check if the id exists
    #if it doesn't:
        #say that the student doesn't exist
        #end the function
    #if it does:
        #remove the student from the list of students
        #return the list of students


#function to view a student's record
def student_record():
    #ask the user what the id is of the student they want to view
    print("What is the ID of the student you want to view?")
    find_id = int(helper.check_num())
    #check if the id exists
    #if it doesn't:
        #say the student doesn't exist
        #end the function
    #if it does:
        #print the student and their information
    pass


#function to edit a student
def edit_student():
    #ask the user what the id is of the student they want to view
    #check if the id exists
    #if it doesn't:
        #say that the student doesn't exist
        #end the function
    #if it does exist:
        #while true loop
            #show the student
            #ask the user what they want to edit (name, student ID, grades) or if they want to exit
            #if they want to edit the name:
                #ask the user what the new name for the student will be
                #set it to the student's name in the dictionary
            #elif they want to edit the student ID:
                #ask the user what the new student ID for the student will be
                #set it to the student's id in the dictionary
            #elif they want to edit the grades:
                #show the grades
                #ask what grade they want to edit (it will be labeled Grade 1, Grade 2, Grade 3, etc...)
                #if the grade doesn't exist, tell the user and continue with the loop
                #if the grade does exist:
                    #ask the user what the new grade will be
                    #set the new grade for the grade that the user selected
            #elif they want to leave:
                #break out of the while loop
            #else if they typed something in that wasn't valid:
                #tell the user that it isn't an option
        #return the student
    pass