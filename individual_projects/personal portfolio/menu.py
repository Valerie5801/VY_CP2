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
root.geometry("1000x765+250-50")
#set window above all other open applications
root.attributes("-topmost", True)

#set up the title, welcome text, buttons, and description window.
title = tk.Label(root, text="Valerie's Programming Portoflio", font=("Times New Roman", 30, "bold"))
title.grid(row=0, column=0, columnspan=2)
"""start = tk.Label(root, text="Yummers")
start.grid(row=0, column=0, columnspan=2)

def change_text():
    start["text"] = fake.word()

test_button = tk.Button(root, text="Change Word", command=change_text)
test_button.grid(row=4, column=0)"""

root.mainloop() #keep program running