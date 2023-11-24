#change this to be a text file so it remembers you settings
#add users so the settings can be save to users
#maybe add passwords and look into encryption
#add verification when person enters email,phone number, or disord


from tkinter import *
import tkinter as tk                                                       
from PIL import Image, ImageTk

class Settings():
    def __init__(self):
        self.size = 50
        self.auto_queen = False

        self.scale_buttons = .3
        self.scale_labels = .3
        self.scale_font = .2

    #state = 'normal', 'iconic', 'withdrawn', or 'zoomed'

    def update_setting_variables(self, key, value):
        self.key = value


    


    def change_color(self, color):
        if color == [120,120,120]:
            color = [169,169,169]
        elif color == [169,169,169]:
            color = [120,120,120]
        return color[0], color[1], color[2]

    

    def add_setting(self, s, setting_name, num_settings, scale_buttons, scale_labels, scale_font, from_rgb, bg_color, *args):
        setting_frame = Frame(s, bg = from_rgb(bg_color),bd = 10)
        setting_frame.pack(side=TOP, fill=X)

        setting_lbl = Label(setting_frame, text = f"{setting_name}: ", width=int(.5*scale_labels*self.size), height=int(.04*self.size),font=('Helvatical bold',int(2*scale_font*self.size)), bg = from_rgb(bg_color),fg = 'black', pady = 10)
        setting_lbl.pack(side=LEFT)
        bg_color[0], bg_color[1], bg_color[2] = self.change_color(bg_color)

        for arg in args:
            exec(f"{setting_name}_{arg} = tk.Button(setting_frame, text = '{arg}', width=int(scale_buttons*self.size), height=int(.03*self.size),font=('Helvatical bold',int(scale_font*self.size)), bg = 'teal', fg = 'black', pady = 10,)")# command= lambda: self.update_setting_variables({setting_name},40))")
            exec(f"{setting_name}_{arg}.pack(side=LEFT, padx=5)")


    def open_settings_window(self, r, from_rgb, exit_settings):
        r.state('iconic')
        
        s = tk.Tk() 
        s.title('Settings') 
        s.geometry('700x600-0+0')
        s.config(bg = 'black')

        s.protocol("WM_DELETE_WINDOW", lambda: exit_settings(r,s))

        bg_color = [169,169,169]

        main_frame = Label(s, bg = from_rgb((100,200,100)),bd = 10)
        main_frame.pack(side=TOP, fill=X)

        exit_button = Button(main_frame, text='Exit', width=7, height=3,font=('Helvatical bold',20), bg = 'teal', fg = 'black', command= lambda: exit_settings(r,s)) 
        exit_button.pack(fill=X) 
        
        self.add_setting(s,'auto_queen', 3, self.scale_buttons, self.scale_labels, self.scale_font, from_rgb, bg_color)
        self.add_setting(s,'full_screen', 3, self.scale_buttons, self.scale_labels, self.scale_font, from_rgb, bg_color)
        self.add_setting(s,'color', 3, self.scale_buttons, self.scale_labels, self.scale_font, from_rgb, bg_color)
