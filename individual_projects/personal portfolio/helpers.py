import sys
from pathlib import Path

#make path directory so python knows where to find the files
sys.path.insert(0, str(Path(__file__).parent.parent))

#import all menu functions for the four projects here
from fractal_pattern_generator import user_menu as fractal
from geometry_calculator import user_menu as geometry
from simple_gradebook import user_menu as gradebook
from word_counter import user_menu as words

#dictionary of info descriptions of each project
project_info = {
    "project_one": "here's a description.",
    "project_two": "here's another description.",
    "project_three": "here's umm idk what to say",
    "project_four": "final description!" 
}

# Simple state tracker using a dictionary
state = {"current_project": None}

#function to show a description of the project with parameters of the project number
def show_desc(project_name, label):
    state["current_project"] = project_name
    label.config(text=project_info[project_name])

#function to run the program of the project with parameters of the project number.
def run_program(root):
    if state["current_project"] is None:
        return
    
    root.withdraw()
    root.attributes("-topmost", False)

    try:
        if state["current_project"] == "project_one":
            fractal.main_menu()
        elif state["current_project"] == "project_two":
            geometry.main_menu()
        elif state["current_project"] == "project_three":
            gradebook.main_menu()
        elif state["current_project"] == "project_four":
            words.main_menu()

    finally:
        root.attributes("-topmost", True)
        root.deiconify()
        root.lift()