# Advanced Functions
# Default Arguments
# *Args
# ## Kwargs

# Project Goal
# make a unit converter


# arguments of functions can be give default values so that the user doesn't necessarily need to provide
# every single argument value
#
# #*args: Many Positional arguments
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# print(add(1, 2, 3, 4, 5))
#
# # What is we wanted to refer to our arguments by names and not by position
# # **kwargs: Many Keyworded Arguments
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     # for k, v in kwargs.items():
#     #     print(f"{k} = {v}")
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)
#
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         # using get allows for None to return for values that haven't been established.
#
# my_car = Car(make="Ford", model="Mustang")
# print(my_car.make, my_car.model)



# Tkinter helps make Graphical User Interface (GUI)
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = tkinter.Label(window, text="I Am a Label", font = ("Arial", 20, "bold"))
my_label["text"] = "New Text"
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)


#Button
def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text = new_text)

button =  tkinter.Button(text = "Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button =  tkinter.Button(text = "Don't click Me")
new_button.grid(column=2, row=0)
# Entry
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=2)



window.mainloop()