#VY 2nd Shape Classes for Geometry Calculator
#import math
import math

#make a class for each shape: circle, rectangle, triangle. Make a subclass for square

#class rectangle here:
class Rectangle:
    #initialize method with parameters length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width
        #use self.[parameter name] and set it to the corresponding parameter to store it

    #make another method to calculate perimeter of the rectangle:
    def calc_peri(self):
        #add self.length and self.width and set it to half_peri
        #multiply half_peri by 2 to and set it to perimeter
        #return the perimeter
        self.perimeter = (self.length + self.width)*2
        return self.perimeter

    #make a method to calculate area of the rectangle:
    def calc_area(self):
        #multiply self.length and self.width and set it to area
        #return the area
        self.area = self.length*self.width
        return self.area

    #method to save info as a dictionary in preperation for storing it in main list:
    def save_info(self):
        #set third and fourth measurements to 0 since they don't exist. They still need to be here for the sake of CSV saving
        rectangle_info = {"Type": "Rectangle", "First Measurement": self.length, "Second Measurement": self.width, "Third Measurement": 0, "Fourth Measurement": 0, "Perimeter": self.perimeter, "Area": self.area}
        return rectangle_info


#square class:
class Square:
    #initialize method with parameters of side:
    def __init__(self, side):
        self.side = side
        #store the side

    #make another method to calculate perimeter of the square:
    def calc_peri(self):
        #multiply the side by four and return it
        self.perimeter = self.side*4
        return self.perimeter
    
    #make another method to calculate area:
    def calc_area(self):
        #square the side and return it
        self.area = self.side**2
        return self.area

    #method to save info as a dictionary in preperation for storing it in main list:
    def save_info(self):
        #set second, third, and fourth measurements to 0 as they don't exist
        square_info = {"Type": "Square", "First Measurement": self.side, "Second Measurement": 0, "Third Measurement": 0, "Fourth Measurement": 0, "Perimeter": self.perimeter, "Area": self.area}
        return square_info


#circle class:
class Circle:
    #initialize with parameter radius:
    def __init__(self, radius):
        self.radius = radius
        #use self.radius and set it to radius
    
    #make a method to calculate perimeter:
    def calc_peri(self):
        #multiply the radius by 2 and pi (accessed via the math module) and set it to perimeter
        #return perimeter
        self.perimeter = self.radius*2*math.pi
        return self.perimeter

    #make a method to calculate area:
    def calc_area(self):
        #square the radius and multiply it by pi and set it to area
        #return area
        self.area = (self.radius**2)*math.pi
        return self.area

    #method to save info as a dictionary in preperation for storing it in main list:
    def save_info(self):
        #set second, third, and fourth measurements to 0 as they don't exist
        circle_info = {"Type": "Circle", "First Measurement": self.radius, "Second Measurement": 0, "Third Measurement": 0, "Fourth Measurement": 0, "Perimeter": self.perimeter, "Area": self.area}
        return circle_info


#triangle class:
class Triangle:
    #initialize with parameters base, first side, second side, and triangle height:
    def __init__(self, base, left_side, right_side, height):
        self.base = base
        self.left_side = left_side
        self.right_side = right_side
        self.height = height
        #use self.[parameter name] and set it to the corresponding parameter to store it

    #make a method to calculate perimeter:
    def calc_peri(self):
        #add the base, first side, and the second side. Set it to perimeter.
        #return perimeter
        self.perimeter = self.base+self.left_side+self.right_side
        return self.perimeter

    #make a method to calculate area:
    def calc_area(self):
        #multiply the base and the triangle height, then divide it by two. Set it to area
        #return area
        self.area = (self.base*self.height)/2
        return self.area

    #method to save info as a dictionary in preperation for storing it in main list:
    def save_info(self):
        #set second, third, and fourth measurements to 0 as they don't exist
        triangle_info = {"Type": "Triangle", "First Measurement": self.base, "Second Measurement": self.left_side, "Third Measurement": self.right_side, "Fourth Measurement": self.height, "Perimeter": self.perimeter, "Area": self.area}
        return triangle_info