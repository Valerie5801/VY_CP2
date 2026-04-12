#import all menu functions for the four projects here
from fractal_pattern_generator import user_menu as fractal
from geometry_calculator import user_menu as geometry
from simple_gradebook import user_menu as gradebook
from word_counter import user_menu as words

#dictionary of info descriptions of each project. this allows the helper function that prints out different text per button to be modular.
project_info = {
    "project_one": "here's a description.",
    "project_two": "here's another description.",
    "project_three": "here's umm idk what to say",
    "project_four": "final description!" 
}

#function to show a description of the project with parameters of the project number
def show_desc(project_name, label):
    label["text"] = project_info[project_name]

#function to run the program of the project with parameters of the project number.
def run_program(root):
    