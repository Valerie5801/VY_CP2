import tkinter as tk
#from helpers import *
from faker import Faker

root = tk.Tk()

fake = Faker()

#make the title
root.title("Valerie's Personal Programming Portfolio")
root.configure()
#lock the window's boundaries to make sure everything stays in place.
root.resizable(False, False)
#set window's boundaries and starting location
root.geometry("1000x770+250-50")
#set window above all other open applications
root.attributes("-topmost", True)

#set up the title, welcome text, buttons, and description window.
title = tk.Label(root, text="Valerie's Programming Portoflio", font=("Times New Roman", 30, "bold"))
title.grid(row=0, column=0, columnspan=2)

welcome_txt = tk.Label(root, text='This is my programming portfolio of the four best projects I have. Click on one of the buttons below to learn more about a project, then press "Run Project" to test it out yourself!')
welcome_txt.grid(row=3, column=0, columnspan=2)

project_one = tk.Button(root, text="Project 1")
project_one.grid(row=6, column=0)
project_two = tk.Button(root, text="Project 2")
project_two.grid(row=6, column=1)
project_three = tk.Button(root, text="Project 3")
project_three.grid(row=8, column=0)
project_four = tk.Button(root, text="Project 4")
project_four.grid(row=8, column=1)

info_box = tk.Label(root, text="Click on one of the buttons to see a description of the project!")
info_box.grid(row=10, column=0, columnspan=3)

run_btn = tk.Button(root, text="Run Program")
run_btn.grid(row=14, column=0, columnspan=2)

root.mainloop() #keep program running
