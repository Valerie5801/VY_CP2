#VY 2nd Classes Notes

#example 1
class Dog:
    def __init__(self, name, breed, age):
        self.name = name.capitalize()
        self.breed = breed.title()
        self.age = age

    def __str__(self):  #happens anytime object is printed
        return f"Name: {self.name}\nBreed: {self.breed}\nAge: {self.age}"
    
    def speak(self):   #needs to be placed at the end of object name since it isn't prebuilt
        return f'{self.name}: "bark"'

doug = Dog("Doug", "Golden Retreiver", 3)
hector = Dog("Hector", "o", 2)

"""print(doug)
print(hector)

print("")

print(doug.speak())
print(doug.speak())
print(hector.speak())
print(doug.speak())
"""

#example 2
class ClassSubject:
    def __init__(self, name = None, room = None, teacher = "Ms. LaRose"):
        self.name = name.title()
        self.room = room
        self.teacher = teacher.title()

    def __str__(self):
        return f"Name: {self.name}\nRoom: {self.room}\nTeacher: {self.teacher}"
    