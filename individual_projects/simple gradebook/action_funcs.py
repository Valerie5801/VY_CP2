#VY 2nd Action Functions for Simple Gradebook

#function to add a student
def add_student():
    #ask the user the name of the student
    #ask the user for the student id (make sure it's a number by using the helper function that stupidproofs numbers)
    #use the Student class (found from the classes.py file) with the information
    #return the student
    pass


#function to add a grade to an existing student
def add_grade():
    #ask the user what the id is of that student
    #check if the id exists
    #if it doesnt:
        #say that the student doesn't exist
        #end the function
    #if it does exist:
        #ask the user for the new grade of the student.
        #add it to the list of grades in the student's dictionary
        #return the student
    pass


#function to remove a student
def remove_student():
    #ask the user what the id is of that student
    #check if the id exists
    #if it doesn't:
        #say that the student doesn't exist
        #end the function
    #if it does:
        #remove the student from the list of students
        #return the list of students
    pass


#function to view a student's record
def student_record():
    #ask the user what the id is of the student they want to view
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


#function to view all students with a parameter of the gradebook
def all_students():
    #as the gradebook should be an object, use the method to show all students
    pass