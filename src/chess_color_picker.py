
from tkinter import *
from tkinter import ttk
import tkinter as tk                                                      
from PIL import Image, ImageTk, ImageDraw
from colorsys import hls_to_rgb as convert_hls_to_rgb



def create_color_picker_frame(master, setting, attribute):
    color_picker_frame = Frame(master, bg=master['bg'])
    color_picker_frame.pack(side=RIGHT)

    hue_var = tk.DoubleVar(value=0.5)
    saturation_var = tk.DoubleVar(value=1)
    lightness_var = tk.DoubleVar(value=0.5)

    create_color_picker_widgets(color_picker_frame, hue_var, saturation_var, lightness_var, setting, attribute)

def create_color_picker_widgets(frame, hue_var, saturation_var, lightness_var, setting, attribute):
    # Color Preview
    color_preview = tk.Button(frame, text=f"use custom\ncolor", bg="light grey", width=20, height=5, command= lambda: get_rgb(frame, hue_var, saturation_var, lightness_var, setting, attribute))
    color_preview.grid(row=0, rowspan=2, column=3, padx=(5,15), pady=2)

    # Hue Scale
    hue_label = Label(frame, text="Hue:", bg=frame['bg'])
    hue_label.grid(row=0, column=0, padx=10, pady=2)
    hue_scale = ttk.Scale(frame, from_=0, to=1, variable=hue_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    hue_scale.grid(row=1, column=0, padx=10, pady=2)

    # Saturation Scale
    saturation_label = Label(frame, text="Saturation:", bg=frame['bg'])
    saturation_label.grid(row=0, column=1, padx=10, pady=2)
    saturation_scale = ttk.Scale(frame, from_=0, to=1, variable=saturation_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    saturation_scale.grid(row=1, column=1, padx=10, pady=2)

    # Lightness Scale
    lightness_label = Label(frame, text="Lightness:", bg=frame['bg'])
    lightness_label.grid(row=0, column=2, padx=10, pady=2)
    lightness_scale = ttk.Scale(frame, from_=0, to=1, variable=lightness_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    lightness_scale.grid(row=1, column=2, padx=10, pady=2)

    # # Get RGB Button
    # rgb_button = ttk.Button(frame, text="Get RGB", command=lambda: get_rgb(frame, hue_var, saturation_var, lightness_var))
    # rgb_button.grid(row=4, columnspan=2, pady=10)

def update_color(frame, hue_var, saturation_var, lightness_var, color_preview):
    hue = hue_var.get()
    saturation = saturation_var.get()
    lightness = lightness_var.get()

    rgb_color = hls_to_rgb(hue, lightness, saturation)
    hex_color = rgb_to_hex(rgb_color)

    color_preview.config(background=hex_color, text = f"Use Color\n{rgb_color}")

def hls_to_rgb(h, l, s):
    r, g, b = convert_hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_rgb(frame, hue_var, saturation_var, lightness_var, setting, attribute):
    hue = hue_var.get()
    saturation = saturation_var.get()
    lightness = lightness_var.get()
    

    rgb_color = hls_to_rgb(hue, lightness, saturation)
    print(f"RGB: {rgb_color}")
    setattr(setting, attribute, rgb_color)
    # button.config(bg=rgb_to_hex(rgb_color))

# def create_main_window():


#     command=lambda: create_color_picker_frame(main_window)
    

#     main_window = tk.Tk()
#     main_window.title("Main Window")

#     color_picker_frame = ttk.Frame(main_window)
#     color_picker_frame.pack(pady=20)

#     open_picker_button = ttk.Button(main_window, text="Open Color Picker", command=lambda: create_color_picker_frame(main_window))
#     open_picker_button.pack(pady=20)

#     main_window.mainloop()

# if __name__ == "__main__":
#     create_main_window()