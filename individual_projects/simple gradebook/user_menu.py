#VY 2nd Main Menu for Simple Gradebook
import action_funcs as act
from classes import GradeBook
import helper

def main_menu():
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
    helper.dict_to_class(gradebook)

    while True:
        print("MAIN MENU")
        student_counter = helper.count_students(gradebook)
        print(f"{student_counter} students are in the gradebook.")

        #ask the user what they want to do. run the corresponding function from action_funcs, and sanitize for invalid inputs
        print("You can: \n\t1. Add new student\n\t2. Add a grade to a student\n\t3. Remove a student\n\t4. View a student's record\n\t5. Edit a student\n\t6. View all students/gradebook\n\t7. Exit")
        print('Please type in numerical input such as 1 for "Add new student"')
        user_action = input("What do you want to do?: ")
        
        match user_action:
            case "1":
                new_student = act.add_student()
                gradebook.add_student(new_student)
            case "2":
                #find the student and run add_grade with the student
                student = helper.ask_id(gradebook)
                if student:
                    student = act.add_grade(student)
            case "3":
                #find the student and run remove_student with the student
                student = helper.ask_id(gradebook)
                if student:
                    act.remove_student(gradebook, student)
            case "4":
                #find the student and run student_record with the student
                student = helper.ask_id(gradebook)
                if student:
                    act.student_record(student)
            case "5":
                #find the student and run edit_student with the student
                student = helper.ask_id(gradebook)
                if student:
                    student = act.edit_student(student)
            case "6":
                #use the show_students method from the GradeBook class
                gradebook.show_students()
            case "7":
                break
            case _:
                print("That isn't an option. Please type a numerical input to select your action.")

        #rewrite CSV after each loop
        for student in gradebook.student_list:
            student.find_avg()
            student.letter_average()
        helper.rewrite_csv(gradebook.student_list)
