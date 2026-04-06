import tkinter as tk

root = tk.Tk() #main window

root.title("wonderhoy")
root.configure(background="purple")
root.minsize(250, 250)
root.maxsize(1500,1500)
root.geometry("300x300+100+100") #top left corner is starting point. This makes a 300x300 window and moves it 100

#font=("[font family]", [font size])
start = tk.Label(root, text="welcome to headspace", font=("Times New Roman", 30, "bold"))  #.pack makes it appear on the screen
start.config(fg="white", background="purple") #fg stands for foreground and changes color of text
start.grid(row=0, column=0, columnspan=2)

#making a counter
root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count) #update the label

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)
    

#use .grid to change position. You need to put this on EVERYTHING even if you only wanna change 1
#don't use .pack if using .grid
add_btn = tk.Button(root, text="ADD", command=add)
add_btn.grid(row=4, column=0)
subt_btn = tk.Button(root, text="SUBTRACT", command=sub)
subt_btn.grid(row=4, column=1)

lbl = tk.Label(root, text="0")
lbl.grid(row=5, column=0, columnspan=2)

close = tk.Button(root, text="goo bye", command = root.destroy)
close.grid(row=6, column=1)

root.mainloop() #keeps program running

