import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Set the theme to 'clam'
style = ttk.Style()
style.theme_use('default')

# Create a DoubleVar to store the scale value
scale_var = tk.DoubleVar()

# Create a ttk.Scale widget
scale = ttk.Scale(root, from_=0, to=100, variable=scale_var, orient="horizontal", length=200)
scale.pack()

# Function to print the scale value when it changes
def scale_changed(value):
    print("Scale value:", value)

# Set the command to call scale_changed function when the scale value changes
scale.config(command=lambda value: scale_changed(scale_var.get()))

root.mainloop()
