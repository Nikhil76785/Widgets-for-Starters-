from tkinter import *
from datetime import date

window = Tk()
window.title("Get Started With Widgets")
window.geometry("400x300")

label = Label(text="Hi there!", fg="white", bg="#072F5F", height=1, width=300)
name_label = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

button = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

label.pack()
name_label.pack()
name_entry.pack()
text_box.pack()
button.pack()

window.mainloop()