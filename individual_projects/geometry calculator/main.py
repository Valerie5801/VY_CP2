#VY 2nd Main for Geometry Calculator
#import user_menu
import action_funcs

#greet user and explain how this program works and what it is.
#run the user_menu function

#thank the user for using the program
shape = action_funcs.create_shape()
shape.calc_peri()
shape.calc_area()
print(shape.show_info())