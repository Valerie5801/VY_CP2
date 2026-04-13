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
    "project_one": "This project generates a sierpinski triangle based on the user's choice of color and depth.\nWhat I learned:\n\t-How to use recursion for shorter, easier to read code.\n\t-How to use turtle to check available colors.\nProgramming Challenges Overcome:\n\t-Recursion logic\n\t-Sanitizing user inputs",
    "project_two": "This project lets users create four different shapes: rectangles, squares, circles, and triangles. It lets users choose the size of the shapes, compare shapes, view shapes, scale shapes, and it saves shapes between ruuns.\nWhat I learned:\n\t-How to use classes for organization and readability of code\n\t-How to save object/class information in a CSV\nProgramming Challenges Overcome:\n\t-Proper formatting so class information will save to a CSV\n\t-Making an intuitive UI",
    "project_three": "This project lets users add, remove, view, and edit students into the gradebook, as well as view the whole class.\nWhat I learned:\n\t-Aggregating classes and utilizing child and parent classes\nProgramming Challenges Overcome:\n\t-Managing information and data/CSV saving\n\t-Figuring out how to get the searching function to work",
    "project_four": "This project lets users type words into a document, view that document, update the document file path in case they change the file they want to look at(must be a .txt file), and rewrite document (which replaces all existing info in the document with new info).\nWhat I learned:\n\t-How to use both a text document and a CSV document to save information\nProgramming Challenges Overcome:\n\t-Figuring out how to use the text document and CSV document to save any changes the user made" 
}

#variable to hold what is currently selected
current_project = {"value": None}

#function to show a description of the project with parameters of the project number
def show_desc(project_name, label):
    #set the selected project to the current project
    current_project['value'] = project_name
    #change the text to the description in the dictionary
    label.config(text=project_info[project_name])

#function to run the program of the project with parameters of the project number.
def run_program(root, label):
    #as a failsafe, if current_project is none, tell the user that they need to select a project before trying to run anything
    if current_project['value'] is None:
        label.config(text="You need to select a project first!")
        return
    
    #hide the window
    root.withdraw()
    root.attributes("-topmost", False)

    try:
        #run the respective project based on what the current project is.
        if current_project['value'] == "project_one":
            fractal.main_menu()
        elif current_project['value'] == "project_two":
            geometry.main_menu()
        elif current_project['value'] == "project_three":
            gradebook.main_menu()
        elif current_project['value'] == "project_four":
            words.main_menu()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        label.config(text=f"An error occurred: {str(e)}\nPlease check the terminal for details.")

    finally:
        #show the window
        root.attributes("-topmost", True)
        root.deiconify()
        root.lift()