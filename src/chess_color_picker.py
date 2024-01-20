
from tkinter import *
from tkinter import ttk
import tkinter as tk                                                      
from PIL import Image, ImageTk, ImageDraw
from colorsys import hls_to_rgb as convert_hls_to_rgb



def create_color_picker_frame(master, setting, button):
    color_picker_frame = Frame(master)
    color_picker_frame.place(x=50,y=50)

    hue_var = tk.DoubleVar()
    saturation_var = tk.DoubleVar()
    lightness_var = tk.DoubleVar()

    create_color_picker_widgets(color_picker_frame, hue_var, saturation_var, lightness_var, setting, button)

def create_color_picker_widgets(frame, hue_var, saturation_var, lightness_var, setting, button):
    # Color Preview
    color_preview = tk.Button(frame, text=f"move sliders\nfor custom\ncolor", bg="light grey", width=20, height=5, command= lambda: get_rgb(frame, hue_var, saturation_var, lightness_var, setting, button))
    color_preview.grid(row=3, columnspan=2, padx=10, pady=10)

    # Hue Scale
    hue_label = Label(frame, text="Hue:")
    hue_label.grid(row=0, column=0, padx=10, pady=10)
    hue_scale = ttk.Scale(frame, from_=0, to=1, variable=hue_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    hue_scale.grid(row=0, column=1, padx=10, pady=10)

    # Saturation Scale
    saturation_label = Label(frame, text="Saturation:")
    saturation_label.grid(row=1, column=0, padx=10, pady=10)
    saturation_scale = ttk.Scale(frame, from_=0, to=1, variable=saturation_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    saturation_scale.grid(row=1, column=1, padx=10, pady=10)

    # Lightness Scale
    lightness_label = Label(frame, text="Lightness:")
    lightness_label.grid(row=2, column=0, padx=10, pady=10)
    lightness_scale = ttk.Scale(frame, from_=0, to=1, variable=lightness_var, orient="horizontal", command=lambda _: update_color(frame, hue_var, saturation_var, lightness_var, color_preview))
    lightness_scale.grid(row=2, column=1, padx=10, pady=10)

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

def get_rgb(frame, hue_var, saturation_var, lightness_var, setting, button):
    hue = hue_var.get()
    saturation = saturation_var.get()
    lightness = lightness_var.get()
    

    rgb_color = hls_to_rgb(hue, lightness, saturation)
    print(f"RGB: {rgb_color}")

    setting = rgb_color
    button.config(bg=rgb_to_hex(rgb_color))
    frame.destroy()

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
