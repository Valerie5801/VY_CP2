#VY 2nd Shape Classes for Geometry Calculator
#import math

#make a class for each shape: circle, rectangle, triangle. Make a subclass for square

#class rectangle here:
    #initialize method with parameters length and width
        #use self.[parameter name] and set it to the corresponding parameter to store it

    #make another method to calculate perimeter of the rectangle:
        #add self.length and self.width and set it to half_peri
        #multiply half_peri by 2 to and set it to perimeter
        #return the perimeter

    #make a method to calculate area of the rectangle:
        #multiply self.length and self.width and set it to area
        #return the area

    #method to display all info:
        #return a string that contains the length, width, perimeter, and area

    #method sound:
        #this is for a fail safe (i think)
        #raise NotImplementedError


#square as a subclass of rectangle (to get properties from rectangle):
    #sound method here to get perimeter:
        #multiply one of the sides (either length or width) by four and return it

    #sound method here to get area:
        #square one of the sides and return it.

    #method to display all info:
        #return a string that contains the length, width, perimeter, and area


#circle class:
    #initialize with parameter radius:
        #use self.radius and set it to radius
    
    #make a method to calculate perimeter:
        #multiply the radius by 2 and pi (accessed via the math module) and set it to perimeter
        #return perimeter

    #make a method to calculate area:
        #square the radius and multiply it by pi and set it to area
        #return area

    #method to display all info:
        #return a string that contains the length, width, perimeter, and area


#triangle class:
    #initialize with parameters base, first side, second side, and triangle height:
        #use self.[parameter name] and set it to the corresponding parameter to store it

    #make a method to calculate perimeter:
        #add the base, first side, and the second side. Set it to perimeter.
        #return perimeter

    #make a method to calculate area:
        #multiply the base and the triangle height, then divide it by tow. Set it to area
        #return area

    #method to display all info:
        #return a string that contains the length, width, perimeter, and area