import tkinter as tk
#from helpers import *

root = tk.Tk()

#make the title
root.title("Valerie's Personal Portfolio")
root.configure()
#lock the window's boundaries to make sure everything stays in place.
root.resizable(False, False)
#set window's boundaries and starting location
root.geometry("1000x765+250-50")
#set window above all other open applications
root.attributes("-topmost", True)

root.mainloop() #keep program running