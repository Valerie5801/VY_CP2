#VY 2nd Helper Functions for Simple Gradebook
import csv
from classes import Student

#function to save the CSV for first time when program is ran
def save_csv():
    #try the following:
    try:
        #open the provided students list and set the mode to "r" for reading as sample:
        with open("individual_projects/simple gradebook/docs/gradebook.csv", mode= "r") as sample:
            #read sample and set it to the variable read_list
            read_list = csv.reader(sample)
            #make a variable that grabs the next value in the CSV reader
            next_item = next(read_list)
            #make an empty list called "exist_students"
            exist_students = []
            #Use a for loop here to make a dictionary:
            for line in read_list:
                exist_students.append(
                    {
                        next_item[0]: line[0],
                        next_item[1]: line[1],
                        next_item[2]: line[2],
                        next_item[3]: line[3],
                        next_item[4]: line[4],
                        next_item[5]: line[5],
                        next_item[6]: line[6],
                        next_item[7]: line[7],
                        next_item[8]: line[8],
                        next_item[9]: line[9]
                    }
                )
                #append the dictionary with the respective information (found using index values)
    #except statement here if the try doesn't work:
    except:
        print("The CSV doesn't exist.")
        #show that the csv doesn't exist
        #Return None
        return []
    #else statement:
    else:
        #Return exist_students
        return exist_students
    

#function for rewriting the CSV again. This will be used every time the user makes a change to their library:
def rewrite_csv(students):
    with open("individual_projects/simple gradebook/docs/gradebook.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)   #read through list
        #write the header
        writer.writerow(['Name', 'ID', 'Average Score', 'Average Letter', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6'])
        
        #loop through students
        for student in students:
            #get the student's grades
            grades = student.grade_list[:6]
            #anything blank or nothing is replaced with a dash
            grades += ['-'] * (6 - len(grades))

            #make a list with the student's information in the order that the CSV is set up
            row = [
                student.name,
                student.student_id,
                student.average,
                student.avg_letter
            ]
            #add grades to row
            row.extend(grades)
            #write a row.
            writer.writerow(row)


#function to convert the returned dict from the CSV and turn it into a Student class:
def dict_to_class(gradebook):
    information = save_csv()

    for info in information:
        #make a student class from the information for each student
        student = Student(info['Name'], int(info['ID']))

        #loop through the grades and add them to the Student class
        for i in range(1,7):
            grade_key = f"Grade {i}"
            if info[grade_key] != '-' and info[grade_key] != '':
                #add it to the grade if it exists
                student.add_grade(int(info[grade_key]))

        #get all necessary information for the student
        student.find_avg()
        student.letter_average()

        #add the student to the gradebook.
        gradebook.add_student(student)

    return gradebook


#function to stupid proof numbers:
def check_num():
    #while True loop:
    while True:
        #get an input from the user
        user_num = input("Type here: ")
        #if the input is not a number, ask them again
        try:
            user_num = round(float(user_num), 2)
        except:
            print("That isn't a number. Please try again.")
        #if it is a number, break out of the loop
        else:
            break
    #return the input
    return user_num


#function to count the students:
def count_students(gradebook):
    counter = 0
    #go up 1 for every student that exists
    for student in gradebook.student_list:
        counter += 1
    return counter


#function to check if a student (ID) exists:
def check_id(gradebook, found_id):
    #loop through the gradebook:
        #check if the student's id matches the found_id
        #if it does, return the student
    #return none here as a failsafe if the student doesn't exist
    for student in gradebook.student_list:
        if student.student_id == found_id:
            return student
    return None


#function to ask the user for an id:
def ask_id(gradebook):
    print("Enter student ID:")
    #ask for the student's ID and sanitize
    find_id = int(check_num())
    #make sure the ID exists
    student = check_id(gradebook, find_id)

    #return student if it exists, and None if it doesn't.
    if student is None:
        print("Student was not found.")
        return None
    else:
        return student