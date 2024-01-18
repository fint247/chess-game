from tkinter import *
from tkinter import ttk
import tkinter as tk                                                      
from PIL import Image, ImageTk, ImageDraw

import tkinter.colorchooser as cc

color = cc.askcolor()
def update_geometry(target, source):
    source_geometry = source.geometry()
    target.geometry(source_geometry)

root = tk.Tk()
root.geometry("300x200")

# Create another window
other_window = tk.Toplevel(root)
other_window.geometry("400x300")

# Create a button to update the geometry
update_button = tk.Button(root, text="Update Geometry", command=lambda: update_geometry(other_window, root))
update_button.pack(pady=20)

root.mainloop()
