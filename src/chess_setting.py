#change this to be a text file so it remembers you settings
#add users so the settings can be save to users
#maybe add passwords and look into encryption
#add verification when person enters email,phone number, or disord


from tkinter import *
import tkinter as tk                                                       
from PIL import Image, ImageTk

size = 50
scale_buttons = .3
scale_labels = .3
scale_font = .2
#state = 'normal', 'iconic', 'withdrawn', or 'zoomed'

def update_settings():
    pass

def change_color(color):
    if color == [120,120,120]:
        color = [169,169,169]
    elif color == [169,169,169]:
        color = [120,120,120]
    return color[0], color[1], color[2]

def exit_settings(r,s):
    s.destroy()
    r.state('zoomed')
    r.state('normal')

def add_setting(s,setting_name, num_settings, scale_buttons, scale_labels, scale_font, from_rgb, bg_color):
    exec(f"{setting_name}_frame = Frame(s, bg = from_rgb(bg_color),bd = 10)")
    exec(f"{setting_name}_frame.pack(side=TOP, fill=X)")

    exec(f"{setting_name}_lbl = Label({setting_name}_frame, text = '{setting_name}:', width=int(.5*scale_labels*size), height=int(.04*size),font=('Helvatical bold',int(2*scale_font*size)), bg = from_rgb(bg_color),fg = 'black', pady = 10)")
    exec(f"{setting_name}_lbl.pack(side=LEFT)")
    bg_color[0], bg_color[1], bg_color[2] = change_color(bg_color)

    for x in range(1,num_settings+1):
        exec(f"{setting_name}_{x} = Button({setting_name}_frame, text = '{setting_name} {x}', width=int(scale_buttons*size), height=int(.03*size),font=('Helvatical bold',int(scale_font*size)), bg = 'teal', fg = 'black', pady = 10)")
        exec(f"{setting_name}_{x}.pack(side=LEFT, padx=5)")

def open_settings(r, from_rgb):
    r.state('withdrawn')
    
    s = tk.Tk() 
    s.title('Settings') 
    s.geometry('700x600-0+0')

    bg_color = [169,169,169]

    main_frame = Label(s, bg = from_rgb((100,200,100)),bd = 10)
    main_frame.pack(side=TOP, fill=X)

    exit_button = Button(main_frame, text='Exit', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command= lambda: exit_settings(r,s)) 
    exit_button.pack(fill=X) 

    add_setting(s,'size', 3, scale_buttons, scale_labels, scale_font, from_rgb, bg_color)
    add_setting(s,'border', 3, scale_buttons, scale_labels, scale_font, from_rgb, bg_color)
    