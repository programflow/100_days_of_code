import tkinter
import tkinter as tk


def convert_miles_to_km():
    distance_miles = float(input.get())
    distance_km = distance_miles * 1.609
    mid_km_text.config(text = f"{distance_km}")


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

mile_label = tk.Label(window, text="Miles", font = ("Arial", 10))
mile_label.grid(column=2, row=0)


left_km_text = tk.Label(window, text = "is equal to")
left_km_text.grid(column=0, row=1)


mid_km_text = tk.Label(window, text = "0")
mid_km_text.grid(column=1, row=1)

right_km_text = tk.Label(window, text = "Km")
right_km_text.grid(column=2, row=1)

input = tk.Entry(width=10)
input.grid(column=1, row=0)

button =  tk.Button(text = "Click Me", command=convert_miles_to_km)
button.grid(column=1, row=2)


window.mainloop()