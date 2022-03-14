import tkinter


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    kilometers_num_label.config(text=f"{round(km, 2)}")


window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

# Miles entry
miles_input = tkinter.Entry(width=9)
miles_input.grid(column=1, row=0)

# Labels
miles_label = tkinter.Label()
miles_label.config(text="Miles", padx=10, pady=10)
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label()
is_equal_label.config(text="is equal to:", padx=10, pady=10)
is_equal_label.grid(column=0, row=1)

kilometers_num_label = tkinter.Label()
kilometers_num_label.config(text="0", padx=10, pady=10)
kilometers_num_label.grid(column=1, row=1)

kilometers_label = tkinter.Label()
kilometers_label.config(text="Km", padx=10, pady=10)
kilometers_label.grid(column=2, row=1)

# Calculate Button
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
