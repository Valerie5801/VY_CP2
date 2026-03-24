#Inheritance

#Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("vroom")


#Child Classes
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("vroom but on water")

class Plane(Vehicle):
    def move(self):
        print("vroom but in the air")

"""car = Car("Ford", "Mustang")
boat = Boat("ibiza", "touring 20")
print(car.brand)
print(car.model)
print(boat.brand)
print(boat.model)
car.move()
boat.move()"""


#Aggregate Classes
class Library:
    def __init__(self, name, catalog = []):
        self.name = name
        self.catalog = catalog
    
    def add_book(self, book):
        self.catalog.append(book)

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.pop(book)
        else:
            print("that book isnt in the catalog")

    def view_catalog(self):
        for book in self.catalog():
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
"""lib = Library("Provo library")
book = Book("Inkheart", "cornelia funke")

lib.add_book("The way of kings", "Brandon sanderson")
lib.add_book("the quest for comets", "david levy")

lib.view_catalog()"""


#Composition
#Child Classes
class Engine:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.engine = Engine("v8")

class Boat(Vehicle):
    def move(self):
        print("vroom but on water")

class Plane(Vehicle):
    def move(self):
        print("vroom but in the air")