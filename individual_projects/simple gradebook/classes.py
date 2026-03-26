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

    #method to return information as a dictionary
    def __str__(self):
        return {'Name': self.name, 'ID': self.student_id, 'Grades': self.grade_list}