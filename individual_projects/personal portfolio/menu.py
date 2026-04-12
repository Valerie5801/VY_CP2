import tkinter as tk
from helpers import show_desc, run_program

def window():
    root = tk.Tk()

    #make the title
    root.title("Valerie's Personal Programming Portfolio")
    root.configure()
    #lock the window's boundaries to make sure everything stays in place.
    root.resizable(False, False)
    #set window's boundaries and starting location
    root.geometry("1000x770+250-50")
    #set window above all other open applications
    root.attributes("-topmost", True)

    #make it so things can properly center
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    #push run button to bottom
    root.rowconfigure(4, weight=1)

    #set up the title, welcome text, buttons, and description window.
    title = tk.Label(root, text="Valerie's Programming Portfolio", font=("Georgia", 40, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=10)

    welcome_txt = tk.Label(root, text='This is my programming portfolio of the four best projects I have. Click on one of the buttons below to learn more about a project, then press "Run Project" to test it out yourself!', font=("Georgia", 15), wraplength=800, justify="center")
    welcome_txt.grid(row=1, column=0, columnspan=2, pady=20, padx=10)

    project_one = tk.Button(root, text="Sierpinski \nTriangle Generator", command=lambda: show_desc("project_one", info_box), font=("Georgia", 15), width=12, height=3)
    project_one.grid(row=2, column=0, padx=13, pady=15)
    project_two = tk.Button(root, text="Shape Calculator", command=lambda: show_desc("project_two", info_box), font=("Georgia", 15), width=12, height=2)
    project_two.grid(row=2, column=1, padx=10, pady=10)
    project_three = tk.Button(root, text="Simple \nGradebook", command=lambda: show_desc("project_three", info_box), font=("Georgia", 15), width=12, height=2)
    project_three.grid(row=3, column=0, padx=10, pady=10)
    project_four = tk.Button(root, text="Word Counter", command=lambda: show_desc("project_four", info_box), font=("Georgia", 15), width=12, height=2)
    project_four.grid(row=3, column=1, padx=10, pady=10)

    #make info box
    info_frame = tk.Frame(root, relief="solid", borderwidth=2, bg="white", width=750, height=450)
    info_frame.grid(row=4, column=0, columnspan=2, padx=30, pady=30)
    info_frame.grid_propagate(False)
    info_frame.columnconfigure(0, weight=1)

    info_box = tk.Label(info_frame, text="Click on one of the buttons to see a description of the project!", font=("Georgia", 10), wraplength=900, justify="center", bg="white")
    info_box.grid(row=0, column=0, padx=10, pady=10)

    #run button at bottom
    run_btn = tk.Button(root, text="Run Program", font=("Georgia"), command=lambda: run_program(root), width=20, height=3)
    run_btn.grid(row=5, column=0, columnspan=2, pady=15, padx=10)

    root.mainloop() #keep program running

window()