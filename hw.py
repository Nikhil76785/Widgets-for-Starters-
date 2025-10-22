from tkinter import *

window = Tk()
window.title("Get Started With Widgets")
window.geometry("400x300")

label = Label(text="Hi there! You can find the product of two numbers in this program", fg="white", bg="#FF0000", height=1, width=300)

name_label1 = Label(text="Enter First Number:", bg="#D15757")
name_entry1 = Entry()
name_label2 = Label(text="Enter Second Number:", bg="#D15757")
name_entry2 = Entry()

def productfunc():
    num1 = float(name_entry1.get())
    num2 = float(name_entry2.get())
    product = num1 * num2
    global message
    message = f"The product of {num1} and {num2} is {product}"

    text_box.insert(END, message)

button = Button(text="Calculate!", command=productfunc, height=1, bg="#1261A0", fg="white")

text_box = Text(height=3)

label.pack()
name_label1.pack()
name_entry1.pack()
name_label2.pack()
name_entry2.pack()
text_box.pack()
button.pack()

window.mainloop()