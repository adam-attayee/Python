#The objective of this exercise is to use tkinter to build a gui that converts miles to kilometers.

import tkinter as tk


def km_converter():
    result = round(float(num_of_miles.get()) * 1.609344, 2)
    result_label.config(text=result)


window = tk.Tk()
window.title("Mile to KM converter")
window.minsize(width=280, height=150)
window.config(padx=40, pady=40)

num_of_miles = tk.Entry(width=10)
num_of_miles.grid(row=1, column=2)

miles_label = tk.Label(text="Miles")
miles_label.grid(row=1, column=3)

equal_label = tk.Label(text="is equal to")
equal_label.grid(row=2, column=1)

result_label = tk.Label(text=" ")
result_label.grid(row=2, column=2)

km_label = tk.Label(text="KM")
km_label.grid(row=2, column=3)

calculate_button = tk.Button(text="Calculate", command=km_converter)
calculate_button.grid(row=3, column=2)

window.mainloop()
