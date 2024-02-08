
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
    # Set the theme
    style = ttk.Style()
    style.theme_use('clam')
    # Color Preview
    color_preview = tk.Button(frame, text=f"custom color\nselector", bg="light grey", width=20, height=5)
    color_preview.config(command= lambda: get_rgb(color_preview, hue_var, saturation_var, lightness_var, setting, attribute))
    color_preview.grid(row=0, rowspan=2, column=3, padx=(5,15), pady=2)
    setting.lyst_of_custom_color.append(color_preview)

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



def update_color(frame, hue_var, saturation_var, lightness_var, color_preview):
    hue = hue_var.get()
    saturation = saturation_var.get()
    lightness = lightness_var.get()

    rgb_color = hls_to_rgb(hue, lightness, saturation)
    hex_color = rgb_to_hex(rgb_color)

    color_preview.config(background=hex_color, text = f"Use Color\n{rgb_color}", state=NORMAL)

def hls_to_rgb(h, l, s):
    r, g, b = convert_hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_rgb(button, hue_var, saturation_var, lightness_var, setting, attribute):
    hue = hue_var.get()
    saturation = saturation_var.get()
    lightness = lightness_var.get()
    

    rgb_color = hls_to_rgb(hue, lightness, saturation)
    # print(f"RGB: {rgb_color}")

    setattr(setting, attribute, rgb_color)
    button.config(bg=rgb_to_hex(rgb_color), text=f"Using Color\n{rgb_color}",state=DISABLED)

