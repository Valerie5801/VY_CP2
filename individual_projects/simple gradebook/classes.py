#VY 2nd Classes for Simple Gradebook
#Use aggregation

#GradeBook Class to manage students with attributes student_list
class GradeBook:
    def __init__(self, student_list = []):
        self.student_list = student_list

    #method to add students
    def add_student(self, student):
        self.student_list.append(student)

    #method to remove students
    def remove_student(self, student):
        if student in self.student_list:
            self.student_list.pop(student)
        else:
            print("That student isn't in the gradebook.")

    #method to show all students
    def show_students(self):
        for student in self.student_list:
            print(student)

    #method to return information
    def save_info(self):
        return self.student_list


#Student Class with attributes name, student_id, and grade_list
class Student:
    def __init__(self, name, student_id, grade_list = []):
        self.name = name
        self.student_id = student_id
        self.grade_list = grade_list

    #method to add a grade
    def add_grade(self, grade):
        self.grade_list.append(grade)

    #method to determine average grade:
    def find_avg(self):
        total = 0
        counter = 0
        #loop through the grade list and add it all up
        for grade in self.grade_list:
            if grade > 0:
                total += grade
                #add one to counter (this will be used for dividing the total by to get average)
                counter += 1

        #get average and round to nearest hundreth
        if counter > 0:
            self.average = round(total/counter, 2)
        else:
            self.average = 0
        return self.average
    
    #method to determine letter average:
    def letter_average(self):
        self.avg_letter = ""

        #check if the average is 0 - meaning there is no grades yet
        if self.average == 0:
            self.avg_letter = "No Grades yet"
        #then check for the rest of the letter grades
        elif self.average >= 90:
            self.avg_letter = "A"
        elif self.average >= 80:
            self.avg_letter = "B"
        elif self.average >= 70:
            self.avg_letter = "C"
        elif self.average >= 60:
            self.avg_letter = "D"
        else:
            self.avg_letter = "F"
        return self.avg_letter

    def __str__(self):
        return f"Name: {self.name}\nID: {self.student_id}\nAverage Grade: {self.average}\nLetter grade: {self.avg_letter}\nGrades: {self.grade_list}"
    
    #method to return information as a dictionary
    def save_info(self):
        return {'Name': self.name, 'ID': self.student_id, 'Average Grade': self.average, 'Letter grade': self.avg_letter, 'Grades': self.grade_list}